# -*- coding: utf-8 -*-
# @File    : 读图.py
# @Date    : 2019-06-20
# @Author  : Zhang.Cookie

import cv2
import numpy as np
from matplotlib import pyplot as plt
#书籍_计算机视觉 (file://DESKTOP-ENP50GA/Users/succful/Desktop/opencvStudy/书籍_计算机视觉)
# path = "C:/Users/succful/Desktop/opencvStudy/书籍_计算机视觉/pic/da.png"

#显示并保存图像（s,esc）
def show():
    img=cv2.imread('./s.png',1)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('./s1.png',img)
#5.1用摄像头捕获视频
def capture():
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        print(cap.read())  #返回是否true
        print(cap.get(3),cap.get(4)) #宽 高
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
    cap.release() #当一切完成时，释放捕获
    cv2.destroyAllWindows()
#capture()

# 5.2 从文件中播放视频
def open_vedio():
    cap = cv2.VideoCapture(0)
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            frame = cv2.flip(frame,0)
             # write the flipped frame
            out.write(frame)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
        # Release everything if job is finished
        cap.release()
        out.release()
        cv2.destroyAllWindows()
# open_vedio()
# 6.1 画线
def line():
    img = np.zeros((512, 512, 3),np.uint8)
    # Draw a diagonal blue line with thickness
    cv2.line(img,(0,0),(511,511),(255,0,0),5)

#line()




















