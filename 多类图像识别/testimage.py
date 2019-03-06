import os,sys
from PIL import ImageGrab
import time
import aircv as ac
from PIL import ImageGrab
import win32api
import win32con
from ctypes import *
import cv2 as cv

# def devicemanager(deviceimage):
#     os.popen("devmgmt.msc")
#     time.sleep(6)
#     ImageGrab.grab().save(deviceimage)
# devicemanager('./pic/oequhhpfu')
# def testclick():
   # windll.user32.SetCursorPos(117,345)er
def clicktest():
    windll.user32.SetCursorPos(120,345)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
clicktest()





