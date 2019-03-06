from tkinter import *
import os
#a = ""
def test(a):
    while True:
        try:
            print(a)

            if a == "":
                print("kong")

            # else:
            #     print(" bu kong")
            if isinstance(int(a[0]),int):
                print(a[0])
                    #break
        except:
            print("失败")
#test("w1")


def test_return(x):
    list=[]
    if x > 0:
        list.append(x)
        return list
    else:
        return 0
# y = test_return(10)
# print(y)


# import tkinter as tk
# import os
# root = tk.Tk()
# # 增加背景图片
# photo = tk.PhotoImage(file="1.gif")
# tk.PhotoImage()
# theLabel = tk.Label(root,
#                 text = "我是内容,\n请你阅读",# 内容
#                 justify = tk.LEFT,# 对齐方式 image = photo,# 加入图片
#                 compound = tk.CENTER,# 关键:设置为背景图片
#                 font = ("华文行楷", 20)),# 字体和字号
#                 #fg ="white") # 前景色
# theLabel.pack()
# tk.mainloop()

#设置背景图片
"""
from tkinter import *
import os
def main():
    filename = "1.gif"
    root = Tk()
    # root.title("尾牙晚宴名单")
    # w = root.winfo_screenwidth()
    # h = root.winfo_screenheight()
    # root.geometry("%dx%d" % (w, h))
    #root.geometry('1000x1000+400+200')
    # root.resizable(False, False)
    img = PhotoImage(file=filename)
    label = Label(root,image=img)
    label.pack()
    root.mainloop()
main()
"""

root = Tk()
Lb1 = Label(root,text="任务要求的OS:").grid(row=0,column=0)
Lb2 = Label(root,text="Driver lastest version :").grid(row=1,column=0)
Lb3 = Label(root,text="Driver previous version :").grid(row=2,column=0)
Ip1 = Entry(root)
Ip2 = Entry(root)
Ip3 = Entry(root)
Ip1.grid(row=0,column=1,padx=10,pady=5)
Ip2.grid(row=1,column=1,padx=10,pady=5)
Ip3.grid(row=2,column=1,padx=10,pady=5)
def show():
    # print("OS：%s"%Ip1.get())
    a = "OS：%s"%Ip1.get()
    b = "lastest：%s" % Ip2.get()
    c = "previous：%s" % Ip3.get()
    # print("lastest：%s"%Ip2.get())
    # print("previous：%s" % Ip3.get())
    return a,b,c
Button(root,text="获取数据",command=show).grid(row=4,column=0,sticky=W,padx=10,pady=5)
Button(root,text="退出",command=root.quit).grid(row=4,column=1,sticky=E,padx=10,pady=5)
root.mainloop()
aa,bb,cc = show()
print(aa)
def write():
    f = open('C:/Users/succful/Desktop/test.txt', 'w')
    f.write(aa)
    f.write("\n"+ bb)
    f.write("\n" + cc)
    f.close()
write()
























