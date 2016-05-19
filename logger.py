# -*- coding: utf-8 -*-

from ctypes import *
import win32gui
import time

user32 = windll.user32
kernel32 =windll.kernel32
psapi = windll.psapi
current_window = None
n = 0

def get_current_process():
    hwnd = user32.GetForegroundWindow()  ##获得前台句柄
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

    print "[PID: %s - %s - %s]" % (process_id,executable.value,window_title.value)
    print window_title1


    ## 关闭句柄
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)


if __name__ == "__main__":
    while n<5:
        get_current_process()
        n += 1
        time.sleep(1)
