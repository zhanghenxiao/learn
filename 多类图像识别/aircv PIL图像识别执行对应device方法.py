# -*- coding: utf-8 -*-
# @File    : aircv PIL图像识别执行对应device方法.py
# @Date    : 2019-01-29
# @Author  : Zhang.Cookie

import aircv as ac
from PIL import Image, ImageGrab
import win32con,win32gui,pyautogui
import win32clipboard as w
def matchImg(imgsrc, imgobj):  # imgsrc=原始图像，imgobj=待查找的图片
    #ImageGrab.grab().save(imgsrc)
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)
    match_result = ac.find_template(imsrc, imobj)
    #'confidence' 匹配相似度，rectangle：匹配图片在原始图像上四边形的坐标
    #result：匹配图片在原始图片上的中心坐标点，也就是我们要找的点击点
    # {'confidence': 0.983245, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
    if match_result is not None:
        match_result['shape'] = (imsrc.shape[1], imsrc.shape[0])  # 0为高，1为宽

    if int((match_result['confidence'])) < int(0.8):
        print("未找到目标图片")
    return match_result
#print(matchImg(imgsrc, imgobj,confidencevalue=0.5))
def main1():

    # imgobj = './edge.png'
    # imgsrc = './imgsrc.png'
    # s = (matchImg(imgsrc, imgobj))
    #print(s)
    imgsrc = './4823.png'
    # for i in range(8):
    imgobj = './0.png'
    s = (matchImg(imgsrc, imgobj))
    print(s)
    if (s['confidence']) > 0.85:
        print()

    #print(s['rectangle'][0][0],s['rectangle'][0][1],s['rectangle'][1][1],s['rectangle'][2][0])
    # x,y,z,w =(s['rectangle'][0][0], s['rectangle'][0][1], s['rectangle'][1][1], s['rectangle'][2][0])
    # bbox = (x,y,z,w)
    # ImageGrab.grab(bbox).save('recap.png')
main1()

def winr():
    # print(pyautogui.size())  #获取屏幕分辨率
    # pyautogui.moveTo(300,300,duration=0.25)
    # pyautogui.moveTo(400, 300, duration=0.25)
    # pyautogui.moveTo(400, 400, duration=0.25)
    # pyautogui.moveTo(300,400,duration=0.25) #移动鼠标
    # x,y = pyautogui.position() #返回当前鼠标位置
    # print(x,y)
    #pyautogui.click(x,y,button="left") #默认左击
    #pyautogui.click(x,y)
    #pyautogui.click(button='right')  # 右击
    #pyautogui.rightClick()             #右击
    #pyautogui.click(button= 'middle') #中击
    # pyautogui.doubleClick(x,y)       #双击
    # pyautogui.scroll(-200)   #滚轮滑动（正数为上，负数为下）
    # pyautogui.dragTo(x,y,duration=0.5) #鼠标拖拽

    # im = pyautogui.screenshot()
    # print(im.getpixel((x,y)))  #300,400这个坐标像素为(103, 73, 112)
    # print(pyautogui.pixelMatchesColor(x,y,(103, 73, 112))) #判断屏幕坐标是否等于这个值
    # print(pyautogui.locateOnScreen('button.png'))  #提前在需点击的位置截图，locateOnScreen简单的颜色对比，不匹配则返回NONE
    # z,w = pyautogui.center(((1, 1039, 41, 36))) #获得中心点
    # pyautogui.click(z,w)


    # pyautogui.click(100,100)
    # pyautogui.typewrite("hello word!") #发送键值
    # pyautogui.hotkey("win","r")  #热键
    #pyautogui.press("win")   #相当于keyDown + keyUp二个函数的整合
    pyautogui.hotkey('alt','tab')
# winr()
class testwin:
    def __init__(self,time):
        self.t = time

    def win(self,time):
        self.t = 100





















