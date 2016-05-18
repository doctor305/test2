import win32api,win32gui, win32con
import win32com.client

shell = win32com.client.Dispatch("WScript.Shell")
shell.Run("calc")
win32api.Sleep(1000)
shell.SendKeys("200{+}")
win32api.Sleep(1000)
shell.SendKeys("{(}100\x2a2{)}")
win32api.Sleep(1000)
shell.SendKeys("-22")
win32api.Sleep(1000)
shell.SendKeys("=")

h = win32gui.FindWindow("SciCalc", None)
edit = win32gui.FindWindowEx(h, None, 'Edit', None)
bufLen = 1024
buf = win32gui.PyMakeBuffer(bufLen)
n = win32gui.SendMessage(edit, win32con.WM_GETTEXT, bufLen, buf)
print buf[0:n]

win32api.Sleep(1000)
win32gui.SendMessage(h, win32con.WM_SYSCOMMAND, win32con.SC_CLOSE, 0)
