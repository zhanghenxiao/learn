from tkinter import *
import tkinter.messagebox as messagebox


def complete():
    nameInput.get()
    nameInput.get()
    messagebox.showinfo('提示', '测试自动运行，请勿进行操作！！')
def printentry():
    print(mefw.get())
    print(bios.get())

root = Tk()
mefw = StringVar()
bios = StringVar()
Ll = Label(root,text='请输入测试的MEFW版本号:')
Ll.pack()
nameInput = Entry(root, borderwidth=8,textvariable=mefw )
nameInput.pack()
L2 = Label(root, text='请输入测试的BIOS版本号:')
L2.pack()
nameInput = Entry(root, borderwidth=8,textvariable=bios )
nameInput.pack()
alertButton = Button(root, text='输入完成，点击确定', command=printentry)
alertButton.pack()

root.geometry('200x200')
root.title(' ')
root.mainloop()




        # def complete(self):
#   name = self.var.get()
#   name = self.var1.get()
#   messagebox.showinfo('提示', '测试自动运行，请勿动！！')
#
#
# def printentry():
#   print(var.get())
#   print(var1.get())
#
# root = Tk()
# var=StringVar()
# var1=StringVar()
# Ll = Label(text='请输入测试的MEFW版本号:')
# Ll.pack()
# Entry(root,textvariable=var).pack() #设置输入框对应的文本变量为var
# L2 = Label(text='请输入测试的BIOS版本号:')
# L2.pack()
# Entry(root,textvariable=var1).pack() #设置输入框对应的文本变量为var
# Button(root,text="输入完毕，请点击确定",command=printentry).pack()
#
#
#
# root.geometry("200x200")
# root.mainloop()