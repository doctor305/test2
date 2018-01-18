# -*- coding: gb2312 -*-

import win32gui
from PIL import ImageGrab
from PIL import Image
import win32con

game_hwnd = win32gui.FindWindow("#32770","大家来找茬")
print game_hwnd



  
win32gui.ShowWindow(game_hwnd, win32con.SW_RESTORE)
# 强行显示界面后才好截图
win32gui.SetForegroundWindow(game_hwnd) # 将游戏窗口提到最前
# 裁剪得到全图
game_rect = win32gui.GetWindowRect(game_hwnd)
print game_rect
src_image = ImageGrab.grab((game_rect[0] + 90, game_rect[1] + 310, 
                            game_rect[2] - 90, game_rect[1] + 310 + 290))
src_image.show()
# 分别裁剪左右内容图片
left_box = (9, 0, 500, 450)
right_box = (517, 0, 517 + 500, 450)
image_left = src_image.crop(left_box)
image_right = src_image.crop(right_box)
image_left.show()
image_right.show()
