import os,sys
from PIL import ImageGrab
import time
import aircv as ac
from PIL import ImageGrab
import win32api
import win32con
from ctypes import *
import cv2 as cv

#os.startfile("C:\Intel")
#os.popen("start C:\Intel")
def chipset(src_path):
    os.system("start C:\Intel\Logs")
    time.sleep(1)
    ImageGrab.grab().save(src_path)
def devicemanager(deviceimage):
    #os.system("devmgmt.msc")
    os.popen("devmgmt.msc")
    time.sleep(6)
    ImageGrab.grab().save(deviceimage)
    print('start')
def control(programimage):
    os.system("Rundll32.exe Shell32.dll,Control_RunDLL appwiz.cpl,,0")
    time.sleep(4)
    ImageGrab.grab().save(programimage)
def find(src,test):
    imsrc = ac.imread(src)
    imsch = ac.imread(test)
    pos = ac.find_template(imsrc,imsch)
    print(pos)
    # x,y = pos['result']
    # reuslt = pos['confidence']
    # #print(pos)
    # if reuslt > 0.2:
    #     print('this is pass')
    # else:
    #     print("this is fail")
    #
    # return (int(x),int(y))
def click(src,test):
    x, y = find(src,test)
    print(x,y)
    windll.user32.SetCursorPos(x, y)
    time.sleep(3)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
if __name__ == '__main__':
  #chipset("./pic/chipset.png")
  #find("./pic/chipset.png","./pic/testchipset.png")
  #time.sleep(2)
  # devicemanager('./pic/device.png')
  # find('./pic/device.png','./pic/VGA.png')
  #time.sleep(2)
  #click('./pic/device.png','./pic/Network.png')
  # time.sleep(2)
  control('./pic/control.png')
  find('./pic/control.png','./pic/mefw.png')




