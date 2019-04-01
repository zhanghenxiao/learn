# -*- coding:utf-8 -*-

import aircv as ac
from PIL import ImageGrab
import win32api
import win32con
from ctypes import *
import cv2 as cv
import sys
import pyautogui


def draw_circle(pos, circle_radius, color, line_width, src_path):
    imsrc = ac.imread(src_path)
    cv.circle(imsrc, pos, circle_radius, color, line_width)
    cv.imshow('objDetect', imsrc)
    cv.waitKey(0)
    cv.destroyAllWindows()

def find_image_cv(obj_path, src_path):
    #ImageGrab.grab().save(src_path)
    pyautogui.screenshot().save(src_path)
    source = cv.imread(src_path)
    template = cv.imread(obj_path)
    result = cv.matchTemplate(source, template, cv.TM_CCOEFF_NORMED)
    pos_start = cv.minMaxLoc(result)[3]
    test = cv.minMaxLoc(result)
    x = int(pos_start[0]) + int(template.shape[1] / 2)
    y = int(pos_start[1]) + int(template.shape[0] / 2)
    similarity = cv.minMaxLoc(result)[1]
    if similarity < 0.85:
        return (-1, -1)
    else:
        print("pass")
        return [(x, y),(x, y)]

def double_click(obj_path, src_path):
    p, q = find_image_cv(obj_path, src_path)
    x, y = p,q
    windll.user32.SetCursorPos(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def main2():
    #找到并双击
    src_path = './pic/destop.png'
    obj_path = './pic/firefox.png'
    print (find_image_cv(obj_path, src_path))
def main1():
    #调试
    circle_radius = 50
    color = (0, 255, 0)
    line_width = 10
    # src_path = './pic/destop.png'
    # obj_path = './pic/firefox.png'
    src_path = './2.png'
    obj_path = './1.png'
    p, circle_center_pos = find_image_cv(obj_path, src_path)
    print(circle_center_pos)

    draw_circle(circle_center_pos, circle_radius, color, line_width, src_path)

    double_click(obj_path, src_path)

if __name__ == "__main__":
    main1()
    #main2()

