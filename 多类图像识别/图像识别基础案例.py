import cv2
import numpy as np
# Alt+3 加注释 ，ALT+4 取注释，TAB 补全
#参考网址：https://blog.csdn.net/wangleixian/article/details/78163745

#path = "C:/Users/succful/Desktop"
# img = cv2.imread("C:/Users/succful/Desktop/574e9258d109b3de52a41f13c6bf6c81800a4cb6.jpg",1)
# cv2.namedWindow("Image")  
# cv2.imshow("Image", img)
# cv2.waitKey (0)
# cv2.destroyAllWindows()
def read(imgpath):#读取图像
    #读取图像有二种 
    img = cv2.imread(imgpath,cv2.COLOR_BGR2HSV) #一 HSV颜色识别-及范围
    img = cv2.imread(imgpath,1) #二 1表示彩色图像，0 表示灰色图像
    cv2.namedWindow("test")
    cv2.imshow("test",img)
    cv2.waitKey (0)
    cv2.destroyAllWindows()
##read("C:/Users/succful/Desktop/haitan-015.jpg")
def imwrite():#保存图像
    img = cv2.imread("C:/Users/succful/Desktop/574e9258d109b3de52a41f13c6bf6c81800a4cb6.jpg",0)
    cv2.imwrite("C:/Users/succful/Desktop/test1.jpg",img,[int(cv2.IMWRITE_JPEG_QUALITY),95])
#imwrite()
def imgcolor():
    img = cv2.imread("C:/Users/succful/Desktop/haitan-015.jpg",cv2.COLOR_BGR2HSV)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_blue=np.array([110,50,50])
    upper_blue=np.array([130,255,255])
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    res=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('hsv',hsv)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('img',img)
    k=res=cv2.waitKey(5)&0xFF
    while k==27:
        break
    cv2.waitKey (0)
    cv2.destroyAllWindows()
##imgcolor()

def hsv():#寻找对象HSV的值
    img = cv2.imread("C:/Users/succful/Desktop/haitan-015.jpg",cv2.COLOR_BGR2HSV)
    green = np.uint8([[[0,255,0]]])
    hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
    print(hsv_green)
def imgsize(): #得到图像值
    img=cv2.imread("C:/Users/succful/Desktop/haitan-015.jpg",cv2.COLOR_BGR2HSV)
    print('图像宽度%d个像素'%(img.shape[1]))
    print('图像高度%d个像素'%(img.shape[0]))
    print('通道数%d个像素'%(img.shape[2]))
    print('显示像素个数%d'%(img.size))
    print(img.max())
    print(type(img))
    cv2.imshow('image',img)
    cv2.waitKey(0)
#imgsize()
def zero(): #画万物
    img=np.zeros((512,512,3),np.uint8)
    cv2.line(img,(0,0),(511,511),(255,0,0),5) #起点，终点，颜色，粗细
    #cv2.rectangle(img,(10,10),(60,60),(0,0,255),5) #画矩形
    #cv2.circle(img,(221,221),63,(0,0,255),-1)  #画圆 -1代表实心
    #font=cv2.FONT_HERSHEY_SIMPLEX#设置字体
    #cv2.putText(img,'Hello OpenCV',(10,50),font,1,(255,255,255),2,cv2.LINE_AA)
    #函数原型：putText(窗口，字符，位置，字体，字体大小，颜色，粗细，线条类型)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#zero()
def mouseevent():#双击画图，并返回坐标
    #events=[i for i in dir(cv2) if 'EVENT' in i] #遍历函数中带有EVENT关键字的语法
    #print(events)
    def draw_circle(event,x,y,flags,param):  
        if event==cv2.EVENT_LBUTTONDBLCLK:  
            cv2.circle(img,(x,y),60,(255,0,0),3)
            print(x,y)
    #img=np.zeros((512,512,3),np.uint8)  
    img=cv2.imread('C:/Users/succful/Desktop/haitan-015.jpg',cv2.COLOR_BGR2HSV)
    cv2.namedWindow('image')  
    cv2.setMouseCallback('image',draw_circle)  
    while(1):  
        cv2.imshow('image',img)  
        if cv2.waitKey(20)&0xFF==27:  
            break  
    cv2.imwrite('C:/Users/succful/Desktop/test.jpg',img)  
    cv2.destroyAllWindows()
#mouseevent()
# >滑动条cv2.creatTrackbar()有五个参数：
#cv2.createTrackbar('R','image',0,255,nothing)
#1：对象名字   2：对象所在面板的名字  3：Trackbar的默认值  4：Trackbar的上调范围（0-count）  5:是调节Trackbar的调用函数
def xiangshu():#获取像素
    img=cv2.imread('C:/Users/succful/Desktop/haitan-015.jpg',cv2.COLOR_BGR2HSV) 
    print(img[50,50])
    hc=img[50,50,0]#获得blue通道值
    hc=img[50,50,1]#获取green通道值
    hc=img[50,50,2]#获取red通道值
#xiangshu()
##img=cv2.imread('C:/Users/succful/Desktop/haitan-015.jpg',cv2.COLOR_BGR2HSV))
##font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8) #Creates a font
##y = image.height / 2 # y position of the text
##x = image.width / 4 # x position of the text 
##cv.PutText(image,"Hello World !", (x,y),font, cv.RGB(255, 255, 255)) #Draw the text 
##cv.ShowImage('Hello World', image) #Show the image
##cv.WaitKey(0)
def mathc_img(image,Target,value):
    img_rgb = cv2.imread(image)
    #创建一个原始图像的灰度版本，所有操作在灰度版本中处理，然后在RGB图像中使用相同坐标还原
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(Target,0)
    #记录图像模板的尺寸,shape会是（1080,1920）很明显这不是我们想要的值,采用倒序的一个处理方法list = [1,2,3] print(list[::-1])
    w, h = template.shape[::-1]
    #使用matchTemplate对原始灰度图像和图像模板进行匹配
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    #设定阀值 threshold = 0.9
    threshold = value
    #res大于90%
    loc = np.where( res >= threshold)
    #使用灰度图像中的坐标对原始RGB图像进行标记
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7,249,151), 2)   
    cv2.imshow('Detected',img_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # image=(".pic/src.png")
    # Target=('.pic/w.png')
    # value=0.9
mathc_img('./pic/src.png','./pic/ww.png',0.9)

#def test(bigimage,smallimage,value):
def test(bigimage,smallimage):
    big = cv2.imread(bigimage,0)
    small = cv2.imread(smallimage,0)
    w,h = small.shape[::-1]
    res = cv2.matchTemplate(big,small,cv2.TM_CCOEFF_NORMED)
    print(res)
    #img_gray = cv2.cvtColor(big, cv2.COLOR_BGR2GRAY)
##    cv2.imshow('Detected', big)
##    cv2.waitKey(0)
##    cv2.destroyAllWindows()
#test("C:/Users/succful/Desktop/big.jpg",'C:/Users/succful/Desktop/small.jpg')
                                                                         









