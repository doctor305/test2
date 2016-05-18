from win32gui import *
ls = []
def foo(hwnd,mouse):
    if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
        ls.append([hwnd,GetWindowText(hwnd)])

EnumWindows(foo,0)
for a in ls:
    if a[1]!='':
        print a[0],a[1]
