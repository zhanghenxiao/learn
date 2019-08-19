# -*- coding: utf-8 -*-
# @File    : 1-15.py
# @Date    : 2019-06-12
# @Author  : Zhang.Cookie

import time

# class test(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age  = age
#     def study(self,study_name):
#         print("%s正在学习%s"%(self.name,study_name))
# w  = test("张先生",20)
# w.study("成功")

# GUI  构架
"""
import tkinter
import tkinter.messagebox


def main():
    flag = True

    # 修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!')\
            if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('240x160')
    # 设置窗口标题
    top.title('小游戏')
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 开启主事件循环
    tkinter.mainloop()


if __name__ == '__main__':
    main()
"""

# 读取文件
def read1():
    try:
        with open('1file.txt','r',encoding='utf-8') as f:
            #print(f.read())
            s = f.read()
            if '分布' in s:
                print('pass')
    except:
        raise ValueError
    else:
        with open('1file.txt', 'r', encoding='utf-8') as f:
            for line in f:
                print(line,end="")
                time.sleep(1)
    finally:
            f.close()
            print('end')
# read1()

import pathlib
# path = pathlib.Path("./lang.txt")
# print(path.name)
# print(path.exists())








