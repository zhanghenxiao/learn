import aircv as ac
from PIL import ImageGrab
import win32api
import win32con
from ctypes import *
import cv2 as cv

# def find():
#     imsrc = ac.imread('./pic/desktop.png')
#     imsch = ac.imread('./pic/firefox.png')
#     # test = ac.find_template(imsrc,imsch)
#     # print(test['result'])
#     # x,y=test['result']
#     pos = ac.find_template(imsrc,imsch)
#     print(pos)
#     x,y = pos['result']
#     return [int(x),int(y)]
# def draw_circle(pos):
#     imsrc = ac.imread('./pic/desktop.png')
#     x, y = pos
#     pos = (x, y)
#     print(x,y)
#     #cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7, 249, 151), 2)
#     #cv.rectangle(imsrc,pos,((0, 1038), (0, 1080), (47, 1038), (47, 1080)),5)
#     cv.circle(imsrc, pos,63,(255,0,0), 5)
#     cv.imshow('objDetect', imsrc)
#     cv.waitKey(0)
#     cv.destroyAllWindows()
# def main():
#     testpos = find()
#     draw_circle(testpos)
#
# if __name__ =="__main__":
#     main()
    #find()

"""
def mathc_img(image,Target,value):
    import cv2
    import numpy as np
    img_rgb = cv2.imread(image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(Target,0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = value
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7,249,151), 2)
    cv2.imshow('Detected',img_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    image = ('./pic/test.png')
    Target = ('./pic/w.png')
    value = 0.9
    mathc_img(image, Target, value)
"""

def read(imgpath):#读取图像
    #读取图像有二种
    img = cv2.imread(imgpath,cv2.COLOR_BGR2HSV) #一 HSV颜色识别-及范围
    img = cv2.imread(imgpath,1) #二 1表示彩色图像，0 表示灰色图像
    cv2.namedWindow("test")
    cv2.imshow("test",img)
    cv2.waitKey (0)
    cv2.destroyAllWindows()