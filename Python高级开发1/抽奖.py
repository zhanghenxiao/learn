
import tkinter
import random
import threading
import time
import os
import xlrd
from datetime import date,datetime

# 初始化窗口
root =tkinter.Tk()
root.title("抽奖名单")
root.geometry('500x500+400+200')
root.resizable(False ,False)
root.flag = True

# 三个Lable标签
first = tkinter.Label(root ,text='' ,font = ("宋体", 20 ,"normal"))
first.place(x=40 ,y=100 ,width=150 ,height=100)

second = tkinter.Label(root ,text='' ,font = ("宋体", 20 ,"normal"))
second['fg'] = 'red'
second.place(x=40 ,y=200 ,width=150 ,height=100)

third = tkinter.Message(root ,text='' ,font = ("宋体", 20 ,"normal"))
third.place(x=40 ,y=300 ,width=150 ,height=100)

four = tkinter.Label(root ,text='' ,font = ("宋体", 20 ,"normal"))
third.place(x=180 ,y=100 ,width=150 ,height=100)

five = tkinter.Label(root ,text='' ,font = ("宋体", 20 ,"normal"))
third.place(x=180 ,y=200 ,width=150 ,height=100)

six = tkinter.Label(root ,text='' ,font = ("宋体", 20 ,"normal"))
third.place(x=180 ,y=300 ,width=150 ,height=100)

#students =['杨姐姐1' ,'杨姐姐2' ,'杨姐姐3' ,'杨姐姐4' ,'杨姐姐5' ,'杨姐姐6']

file = 'cc.xlsx'
def read_excel():
    wb = xlrd.open_workbook(filename=file)#打开文件
    # print(wb.sheet_names())#获取所有表格名字
    sheet1 = wb.sheet_by_index(0)#通过索引获取表格
    # sheet2 = wb.sheet_by_name('工号')#通过名字获取表格
    #print(sheet1)
    #print(sheet1.name,sheet1.nrows,sheet1.ncols) #获取总的行，列数
    cla = sheet1.row_values(0)
    n = cla.index('姓名')
    c = cla.index('课别')
    j = cla.index('工号')
    # print(cla)
    # print(i,n,d)
    # print(type(i))
    name = sheet1.col_values(n)  # 获取列内容
    course = sheet1.col_values(c)  # 获取列内容
    job = sheet1.col_values(j)  # 获取列内容
    # for x in range(sheet1.nrows):
    #     name = (sheet1.cell(x, i).value)
    #     print(name)

def switch():
    wb = xlrd.open_workbook(filename=file)  # 打开文件
    # print(wb.sheet_names())#获取所有表格名字
    sheet1 = wb.sheet_by_index(0)  # 通过索引获取表格
    # sheet2 = wb.sheet_by_name('工号')#通过名字获取表格
    # print(sheet1)
    # print(sheet1.name,sheet1.nrows,sheet1.ncols) #获取总的行，列数
    cla = sheet1.row_values(0)
    n = cla.index('姓名')
    c = cla.index('课别')
    j = cla.index('工号')
    # print(cla)
    # print(i,n,d)
    # print(type(i))
    name = sheet1.col_values(n)  # 获取列内容
    course = sheet1.col_values(c)  # 获取列内容
    job = sheet1.col_values(j)  # 获取列内容
    print(course)
    # for x in range(sheet1.nrows):
    #     name = (sheet1.cell(x, i).value)
    #     print(name)
    root.flag =True
    while root.flag:
        #i=random.randint(0, len(students)-1)
        n1 = random.randint(0,len(name)-1)
        j1 = random.randint(0,len(job)-1)
        first['text']=second['text']
        second['text']=third['text']
        third['text']=name[n1]

        # c1 = random.randint(0,len(course)-1)
        # four['text'] = five['text']
        # five['text'] = six['text']
        # six['text'] = course[c1]
        time.sleep(0.1)


# 开始按钮
def butStartClick():
    t=threading.Thread(target=switch)
    t.start()
btnStart=tkinter .Button(root,text='开 始',command =butStartClick)
btnStart.place(x=30, y=30, width=80, height=20)


# 结束按钮
def btnStopClick():
    root.flag=False

butStop=tkinter.Button(root,text=' 停止',command=btnStopClick)
butStop.place(x=160, y=30, width=80, height=20)

# 启动主程序
root.mainloop()

