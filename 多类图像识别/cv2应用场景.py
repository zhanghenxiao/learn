# # --------获取视频----------
# import cv2
# import numpy as np
# cap=cv2.VideoCapture("E:/cv video/Alan Walker - Darkside.mp4")  #视频采集,路径
# while True:
#     ret,frame=cap.read()
#     frame=cv2.flip(frame,1)#获取第一帧
#     cv2.imshow('test video',frame)  #显示采集到视频在窗口上
#     if cv2.waitKey(60)==ord('x'):    #视频播放速率key里面的参数
#         break
# cap.release()   #停止捕捉视频
# cv2.destroyAllWindows()   #关闭窗口
# -----------获取图片并保存---------------
import cv2
import numpy as np
img=cv2.imread("E:/cv video/timg.jpg",0)
cv2.namedWindow('pic',cv2.WINDOW_AUTOSIZE)
cv2.imshow('pic',img)
k=cv2.waitKey()
if k==27:
    cv2.destroyAllWindows()    #关闭窗口
elif k==ord('x'):
    cv2.imwrite("E:/cv video/timg1.jpg",img)
    cv2.destroyAllWindows()
# import cv2
# import  numpy as np
# # cap.set(propId,value) 来修改视频属性，value 就是你想要设置成的新值。
#
# cap = cv2.VideoCapture(0)
# cap.set(propId=0)
# 0:视频文件的当前位置(毫秒)。
# 1:下面要解码/捕获的基于帧的索引。
# 2:比例相对位置的视频文件:0开始的电影，1结束的电影
# 3:在视频流中帧的宽度宽度。
# 4:视频流中帧的高度。
# 5:FPS帧速率。
# 6:编解码器。
# 7:帧在视频文件中的帧数。
# 8:由retrieve()返回的Mat对象的格式。
# 9:模式后端特定值，指示当前捕获模式。
# 10:图像的亮度(仅用于照相机)。
# 11:图像的对比度(仅对照相机)。
# 12:图像的饱和饱和度(仅对照相机)。
# 13:图像的色调(仅用于照相机)。
# 14:获得图像的增益(仅用于照相机)。
# 15:曝光(仅用于照相机)。
# 16:RGB布尔标志，指示图像是否应该转换为RGB。
# 17:WHITE_BALANCE目前不支持的
# 18:立体声摄像机整流标志(注:只支持DC1394 v2)。x目前后台)


# import cv2
# import numpy as np
# img=cv2.imread("E:/cv video/timg.jpg",1)
# img[180:220,180:280] = [0,0,1]
# print(img.shape)
# print(img.size)
# print(img.dtype)
# cv2.imshow('logo',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#img.shape 可以获取图像的形状。返回值是一个包含行数，列数，通道数的元组。灰度图只返回行数，列数这样一个元组。
# 所以可以用这个来判断图片类型，是彩色图还是灰度图。

#img.size返回图像array数组总的元素个数，对于彩色三通道图，就是行数*列数*3，对于灰度图就是行数*列数。

#img.dtype返回图像的数据类型，也就是array数组的数据类型。
# --------放大缩小图片---------
# import cv2
# import numpy as np
# img=cv2.imread("C:/Users/harrit-working UUT/Desktop/test.jpg")
# height,width=img.shape[:2]
# res=cv2.resize(img,(int(height*0.8),int(width*0.2)),interpolation=cv2.INTER_LINEAR)
# while(1):
#     # cv2.imshow('img',img)
#     cv2.imshow('res',res)
#     if cv2.waitKey(1) & 0XFF ==27:
#         break
# cv2.destroyAllWindows()

import cv2
import numpy as  np
img=np.zeros((512,512,3),np.uint8)
cv2.line(img,(0,0),(0,512),(145,255,4),44)  #X,Y轴，屏幕框大小，颜色,以及像素点大小
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
























