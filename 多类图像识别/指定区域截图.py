# -*- coding: utf-8 -*-
# @File    : 指定区域截图.py
# @Date    : 2019-01-18
# @Author  : Zhang.Cookie

# -*- coding:utf-8 -*-
"""
import tkinter
import tkinter.filedialog
import os
from PIL import ImageGrab
from time import sleep
from tkinter import StringVar, IntVar

# 创建tkinter主窗口
root = tkinter.Tk()
# 指定主窗口位置与大小
root.geometry('200x80+400+300')
# 不允许改变窗口大小
root.resizable(False, False)


class MyCapture:
    def __init__(self, png):
        # 变量X和Y用来记录鼠标左键按下的位置
        self.X = tkinter.IntVar(value=0)
        self.Y = tkinter.IntVar(value=0)

        self.selectPosition = None
        # 屏幕尺寸
        screenWidth = root.winfo_screenwidth()
        # print(screenWidth)
        screenHeight = root.winfo_screenheight()
        # print(screenHeight)
        # 创建顶级组件容器
        self.top = tkinter.Toplevel(root, width=screenWidth, height=screenHeight)
        # 不显示最大化、最小化按钮
        self.top.overrideredirect(True)
        self.canvas = tkinter.Canvas(self.top, bg='white', width=screenWidth, height=screenHeight)
        # 显示全屏截图，在全屏截图上进行区域截图
        self.image = tkinter.PhotoImage(file=png)
        self.canvas.create_image(screenWidth // 2, screenHeight // 2, image=self.image)

        # 鼠标左键按下的位置
        def onLeftButtonDown(event):
            self.X.set(event.x)
            self.Y.set(event.y)
            # 开始截图
            self.sel = True

        self.canvas.bind('<Button-1>', onLeftButtonDown)

        # 鼠标左键移动，显示选取的区域
        def onLeftButtonMove(event):
            if not self.sel:
                return
            global lastDraw
            try:
                # 删除刚画完的图形，要不然鼠标移动的时候是黑乎乎的一片矩形
                self.canvas.delete(lastDraw)
            except Exception as e:
                pass
            lastDraw = self.canvas.create_rectangle(self.X.get(), self.Y.get(), event.x, event.y, outline='black')

        self.canvas.bind('<B1-Motion>', onLeftButtonMove)

        # 获取鼠标左键抬起的位置，保存区域截图
        def onLeftButtonUp(event):
            self.sel = False
            try:
                self.canvas.delete(lastDraw)
            except Exception as e:
                pass
            sleep(0.1)
            # 考虑鼠标左键从右下方按下而从左上方抬起的截图
            myleft, myright = sorted([self.X.get(), event.x])
            mytop, mybottom = sorted([self.Y.get(), event.y])
            self.selectPosition = (myleft, myright, mytop, mybottom)
            #             pic = ImageGrab.grab((left+1, top+1, right, bottom))
            #
            #             #弹出保存截图对话框
            #
            #             fileName = tkinter.filedialog.asksaveasfilename(title='保存截图', filetypes=[('JPG files', '*.jpg')])
            #
            #             if fileName:
            #
            #                 pic.save(fileName+'.jpg')
            # 关闭当前窗口
            # print(left, '  ', top,'  ',right,'  ',bottom)

            self.top.destroy()

        self.canvas.bind('<ButtonRelease-1>', onLeftButtonUp)
        self.canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)
    # 开始截图


text = StringVar()
text.set('old')


def buttonCaptureClick():
    # 最小化主窗口
    # root.state('icon')
    # sleep(0.2)

    filename = 'temp.png'
    im = ImageGrab.grab()
    im.save(filename)
    im.close()
    # 显示全屏幕截图
    w = MyCapture(filename)
    buttonCapture.wait_window(w.top)
    text.set(str(w.selectPosition))

    # print(w.myleft,w.mybottom)
    # 截图结束，恢复主窗口，并删除临时的全屏幕截图文件
    # label.config(text='Hello')
    root.state('normal')
    os.remove(filename)


label = tkinter.Label(root, textvariable=text)
label.place(x=10, y=30, width=160, height=20)
label.config(text='New test')
buttonCapture = tkinter.Button(root, text='截图', command=buttonCaptureClick)
buttonCapture.place(x=10, y=10, width=160, height=20)
# 启动消息主循环
# root.update()
root.mainloop()
"""
"""
import pyHook
import pythoncom
import win32gui
from PIL import Image, ImageGrab
from win32api import GetSystemMetrics as gsm

# 提前绑定鼠标位置事件
old_x, old_y = 0, 0
new_x, new_y = 100, 100
def hotkey(key=None):
    #绑定热键，开始进行划屏截图操作
    pass

def on_mouse_event(event):
    global old_x, old_y, new_x, new_y, full, hm
    if event.MessageName == "mouse left down":
        old_x, old_y = event.Position
    if event.MessageName == "mouse left up":
        new_x, new_y = event.Position # 解除事件绑定
        hm.UnhookMouse()
        hm = None # 划屏
        if full:
            image = ImageGrab.grab((0, 0, gsm(0), gsm(1)))
        else:
            image = ImageGrab.grab((old_x, old_y, new_x, new_y))
        image.show()

full = False
hm = None
def capture():
    hm = pyHook.HookManager()
    hm.SubscribeMouseAll(on_mouse_event)
    hm.HookMouse()
    pythoncom.PumpMessages()
# capture()

# bbox = (534,501,608,603)
# im = ImageGrab.grab(bbox)
# # 参数 保存截图文件的路径
# im.save('as.png')
"""


import aircv as ac
import pytesseract,pyautogui
import win32con,win32api,time,re
from ctypes import *
from PIL import Image, ImageGrab
def matchImg(imgsrc, imgobj,confidencevalue=0.8):  # imgsrc=原始图像，imgobj=待查找的图片
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
def test():
    imgsrc = './2.png'
    imgobj = './1.png'
    s = (matchImg(imgsrc, imgobj, confidencevalue=0.8))
    print(s)
test()
"""
def main1():
    imgsrc = './imgsrc.png'
    imgobj = './firefox.png'
    s = (matchImg(imgsrc, imgobj, confidencevalue=0.8))
    print(s)
    #print(s['rectangle'][0][0],s['rectangle'][0][1],s['rectangle'][1][0],s['rectangle'][1][1])
    x,y,z,w =(s['rectangle'][0][0], s['rectangle'][0][1], s['rectangle'][2][0], s['rectangle'][3][1])
    bbox = (x,y,z,w)   #左上，左下，右上，右下
    print(bbox)
    bbox2 = (x+(z-x),y,z+300,w)
    ImageGrab.grab(bbox).save('recap.png')  #按照指定坐标截图
    ImageGrab.grab(bbox2).save('recap2.png')
main1()

def getstring(strpath):
    text = pytesseract.image_to_string(Image.open(strpath))
    print(text)
    text2 = re.search('(.*/)',text).group()
    text3 = re.search('\d+',text2).group()
    print("运行的圈数为%d"%int(text3))
    with open("s3log.txt","w+") as f:
        f.write(text3)
        f.close()
getstring('./recap2.png')

def double_click(x,y):
    windll.user32.SetCursorPos(x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
def testclick():
    #(474, 452, 473, 621)
    pyautogui.moveTo(404,480)
# testclick()
"""