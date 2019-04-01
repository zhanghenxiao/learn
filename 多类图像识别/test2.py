# -*- coding:utf-8 -*-

import aircv as ac
from PIL import ImageGrab
import win32api
import win32con
from ctypes import *
import cv2 as cv


def draw_circle(pos, circle_radius, color, line_width, src_path):
    imsrc = ac.imread(src_path)
    x, y = pos
    pos = (x, y)
    cv.circle(imsrc, pos, circle_radius, color, line_width)
    cv.imshow('objDetect', imsrc)
    cv.waitKey(0)
    cv.destroyAllWindows()

def find_image_duniang(obj_path, src_path):
    # ImageGrab.grab().save(src_path)  #截图
    imsrc = cv.imread(src_path)
    imobj = cv.imread(obj_path)
    pos = ac.find_template(imsrc,imobj)
    print(pos)
    x, y = pos['result']
    return [int(x), int(y)]

def double_click(obj_path, src_path):
    x, y = find_image_duniang(obj_path, src_path)
    windll.user32.SetCursorPos(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def main1():
    #调试
    circle_radius = 50
    color = (0, 255, 0)
    line_width = 10
    src_path = './1.png'
    obj_path = './2.png'
    circle_center_pos = find_image_duniang(src_path, obj_path)
    print(circle_center_pos)
    draw_circle(circle_center_pos, circle_radius, color, line_width, src_path)

def main2():
    #找到并双击
    src_path = './pic/desktop.png'
    obj_path = './pic/firefox.png'
    print(find_image_duniang(obj_path, src_path))
    double_click(obj_path, src_path)
def click(x, y):
    windll.user32.SetCursorPos(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
if __name__ == "__main__":
    main1()
    #main2()
    #print(find_image_duniang('./pic/desktop.png', './pic/firefox.png'))

