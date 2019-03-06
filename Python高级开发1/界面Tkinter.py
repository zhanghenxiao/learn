import tkinter
from PIL import *
from PIL import Image, ImageTk
from tkinter import *
from PIL import Image,ImageEnhance
import pytesseract
#2018-12-20
"""
root=tkinter.Tk()
root.title('name')#修改框体的名字,也可在创建时使用className参数来命名；
root.resizable(0,0)#框体大小可调性，分别表示x,y方向的可变性；
root.geometry('250x150')# 指定主框体大小；
#root.quit() #退出；
root.update_idletasks()
root.update()       #刷新页面；
root.mainloop()
"""

"""
root = tkinter.Tk() #生成root窗口
root.title('Cookie')
root.geometry('250x150') #窗体大小
label = tkinter.Label(root,text = 'Hello,gui') #生成标签
label.pack() #将标签添加到窗口
button1 = tkinter.Button(root,text= '开始' ) #生成button1
button1.pack(side=tkinter.TOP) #将button添加到root主窗口居上的位置
button1 = tkinter.Button(root,text= '暂停' )
button1.pack(side=tkinter.BOTTOM)
root.mainloop() #进入消息循环（必需组件）
"""

#2018-12-21 label标签的使用（使用图片）
"""
def callback():
    var.set("hhhhhhh")
root = Tk()
root.geometry("600x600")
var = StringVar() #自动刷新字符串变量
var.set("66666")
frame1 = Frame(root)
frame2 = Frame(root)
lb = Label(frame1,textvariable=var,padx=100)
lb.pack(side=LEFT)
# img = Image(file="1.gif",imgtype="photo")
img = PhotoImage(file="./testVGA.png")
lb2 = Label(frame1,image=img)
lb2.pack(side=RIGHT)
btnCm = Button(frame2,text="下一步",command=callback)
btnCm.pack()
frame1.pack()
frame2.pack()
root.mainloop()
"""
# 2018-12-24 checkbutton(1)
"""
root =Tk()
v = IntVar()    #选中为1，未选中为0
c = Checkbutton(root,text="Test",variable=v)
c.pack()
l = Label(root,textvariable=v)
l.pack()
root.mainloop()
"""
#checkbutton(2)
"""
root =Tk()
GIRLS = ["asd",'dsa','fef','fwaf']
v = []
def change():
    for i in v:
        print(i.get())
for girl in GIRLS:
    v.append(IntVar())
    b = Checkbutton(root,text=girl,variable=v[-1],command=change)  #使用一个固有变量来记录状态
    b.pack(anchor=W)    #控件相对主窗口在左边
root.mainloop()
"""
#Radiobutton(1) 对于单选框，多个按钮只对应一个变量，复选框，多个按钮对应多个值
"""
def change():
    print(v.get())
root = Tk()
v = IntVar()
Radiobutton(root,text="one",variable=v,value=1,command=change).pack(anchor=W)
Radiobutton(root,text="two",variable=v,value=2,command=change).pack(anchor=W)
Radiobutton(root,text="three",variable=v,value=3,command=change).pack(anchor=W)
root.mainloop()
"""
#Radiobutton(2)
"""
def change():
    print(v.get())
root = Tk()
v = IntVar()
Langes = [
    ("python",1),
    ("javascript",2),
    ("Lua",3),
    ("Ruby",4)
]
group = LabelFrame(root,text="选择喜欢的语言",padx=5,pady=5)
group.pack(padx=10,pady=10)
for key,val in Langes:
    Radiobutton(group,text=key,variable=v,value=val,command=change).pack(anchor=W)
root.mainloop()
"""
# Entry（1） 文本框(单行)
"""
root = Tk()
input = Entry(root)
input.pack(padx=20,pady=20)
input.delete(0, END)    #先清空按照索引
input.insert(0,"请输入内容...")
root.mainloop()
"""
# Entry（2）
"""
root = Tk()
Lb1 = Label(root,text="作品:").grid(row=0,column=0)
Lb2 = Label(root,text="作者:").grid(row=1,column=0)
Ip1 = Entry(root)
Ip1.grid(row=0,column=1,padx=10,pady=5)
Ip2 = Entry(root)
Ip2.grid(row=1,column=1,padx=10,pady=5)
def show():
    print("作品：《%s》"%Ip1.get())
    print("作者：%s"%Ip2.get())
Button(root,text="获取数据",command=show).grid(row=3,column=0,sticky=W,padx=10,pady=5)
Button(root,text="退出",command=root.quit).grid(row=3,column=1,sticky=E,padx=10,pady=5)
root.mainloop()
"""
# Entry（3）密码设置
"""
root = Tk()
Lb1 = Label(root,text="账号:").grid(row=0,column=0)
Lb1 = Label(root,text="密码:").grid(row=1,column=0)
v1 = StringVar()
v2 = StringVar()
Ip1 = Entry(root)
Ip1.grid(row=0,column=1,padx=10,pady=5)
Ip2 = Entry(root,show="*")
Ip2.grid(row=1,column=1,padx=10,pady=5)
def show():
    print("账号：%s"%Ip1.get())
    print("密码：%s"%Ip2.get())
Button(root,text="获取数据",command=show).grid(row=3,column=0,sticky=W,padx=10,pady=5)
Button(root,text="退出",command=root.quit).grid(row=3,column=1,sticky=E,padx=10,pady=5)
root.mainloop()
"""
# Entry（4)事件处理和数据验证
"""
from tkinter import *
root = Tk()
Lb1 = Label(root,text="账号:").grid(row=0,column=0)
Lb2 = Label(root,text="密码:").grid(row=1,column=0)
def test():
    if Ip1.get() == "root":
        print("正确")
        return True
    else:
        print("错误")
        Ip1.delete(0,END)
        return False
Ip1 = Entry(root,validate="focusout",validatecommand=test)
Ip1.grid(row=0,column=1,padx=10,pady=5)
Ip2 = Entry(root,show="*")
Ip2.grid(row=1,column=1,padx=10,pady=5)
root.mainloop()
"""
#Entry（5）密码设置
"""
root = Tk()
Lb1 = Label(root,text="账号:").grid(row=0,column=0)
Lb1 = Label(root,text="密码:").grid(row=1,column=0)
def test():
    if Ip1.get() == "root":
        print("正确")
        return True
    else:
        print("错误")
        Ip1.delete(0,END)
        return False
def test2():
    print("数据验证失败，我被调用...")
Ip1 = Entry(root,validate="focusout",validatecommand=test,invalidcommand=test2)
Ip1.grid(row=0,column=1,padx=10,pady=5)
Ip2 = Entry(root,show="*")
Ip2.grid(row=1,column=1,padx=10,pady=5)
root.mainloop()
"""

#蛮有趣的验证
"""
# test = ['aa','c0','10','bo']
# for t in  test:
#     print(t)
#     try :
#         print(int(t))
#         if isinstance(int(t),int):
#             print("pass")
#     except ValueError as e:
#         print(e)

# import tkinter as tk
# from PIL import ImageTk, Image
#
# root = tk.Tk()
# root.title("尾牙晚宴名单")
# w = root.winfo_screenwidth()
# h = root.winfo_screenheight()
# root.geometry("%dx%d" %(w,h))
# # 背景
# canvas = tk.Canvas(root, width=1200, height=1200, bd=0, highlightthickness=0)
# imgpath = '1.jpg'
# img = Image.open(imgpath)
# photo = ImageTk.PhotoImage(img)
# canvas.create_image(900,800, image=photo)
# canvas.pack()
# root.mainloop()
"""
# 动图
"""
from PIL import ImageTk,Image
import time
from tkinter import *

def moveImage(event):#图片logo.gif的移动要绑定的函数
  if event.keysym=='Up':
    canvas.move(1,0,-3)#移动ID为1的事物，使得横坐标加0，纵坐标减3
  elif event.keysym=='Down':
    canvas.move(1,0,+3)
  elif event.keysym=='Left':
    canvas.move(1,-3,0)
  elif event.keysym=='Right':
    canvas.move(1,3,0)
  tk.update()
  time.sleep(0.05)
def changeColor(event):
  if event.keysym=='Up':
    canvas.itemconfig(pg,fill='blue')#填充ID为pg的事物，填充为blue
tk=Tk()#窗口
canvas=Canvas(tk,width=400,height=400)#画布
canvas.pack()#显示出来
myImage=PhotoImage(file='./1.gif')#图片格式必须为gif格式
im=canvas.create_image(0,0,anchor=NW,image=myImage)#加载图片
pg=canvas.create_polygon(10,10,10,60,50,35,fill='red')#创建三角形
print (im);print (pg) #显示图片和三角形的ID
canvas.bind_all('<KeyPress-Up>',moveImage)#绑定方向键 up
canvas.bind_all('<KeyPress-Down>',moveImage)
canvas.bind_all('<KeyPress-Left>',moveImage)
canvas.bind_all('<KeyPress-Right>',moveImage)
#canvas.bind_all('<KeyPress-Up>',changeColor)
"""















