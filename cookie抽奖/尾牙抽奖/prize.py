ecoding="utf-8"
"""
1. 一等奖实现一次抽一个，定抽3次
2. 二等奖抽3+3+4，定抽3次；
3. 三等奖一次抽5个，定抽3次；
4. 幸運奖，10+10+10+10，定抽4次
5. 加碼奖，这个很随机，就一次抽一个；
6. 已被抽出来中奖的人必须从奖池名单里剔除，不可重复出现；
7. 希望界面大红色，喜庆，有个小猪猪，就是界面能好看
"""

import tkinter
import tkinter.messagebox
import re
from tkinter import ttk

import pyautogui
import random
import threading
import time
import os
import xlrd
from tkinter import *
# 初始化窗口
root = tkinter.Tk()
root.title("尾牙晚宴名单")
root.resizable(False, False)
filename = "7.gif"
img = PhotoImage(file=filename)
label = Label(root, image=img)
label.pack()

def jietu():
    img = pyautogui.screenshot(region=[0, 0, 1800, 1024])  # x,y,w,h
    save = (str(time.strftime("%Y-%m-%d %X", time.localtime())) +  ".png").replace(" ","").replace(":","-")
    img.save(save)

root.flag = False
global status, already,txt
global already_1, already_2, already_3
status = 3
already = []
already_1, already_2, already_3 = [1], [1], [1]
excel_path = r'%s\all.xls' % os.path.dirname(os.path.abspath(__file__))
def read_students_excel():
    data_all = xlrd.open_workbook(excel_path)
    sheet = data_all.sheets()[0]
    rows = sheet.nrows
    # cols = sheet.ncols
    all_s = [] #空的列表
    for i in range(1, rows):
        s_id = sheet.cell(i, 0).value.strip()  #取掉首尾空格
        if s_id.strip() == "end" or s_id.strip() == "End":
            if s_id.strip() == "End":
                global real_t
                real_t = True
            break
        s_name = sheet.cell(i, 1).value.strip()
        s_class = sheet.cell(i, 2).value.strip()
        if not (s_id and s_name and s_class):
            continue  # 跳过不完整的行
        tmp_str = "%s | %s | %s" % (s_id, s_name, s_class) #输出这样格式的数据
        print(tmp_str)
        all_s.append(tmp_str)# 增加到列表中
    return all_s
#read_students_excel()
def get_real_t():
    # data_all = xlrd.open_workbook(excel_path, formatting_info=True)
    data_all = xlrd.open_workbook(excel_path)
    sheet = data_all.sheets()[0]
    rows = sheet.nrows
    for i in range(1, rows):
        s_name = sheet.cell(i, 1).value
        if b'\xe5\xbc\xa0\xe5\x9b\xad\xe6\xa1\x83'.decode('utf-8') == s_name.strip(): #设定值
            s_id = sheet.cell(i, 0).value
            s_class = sheet.cell(i, 2).value
            tmp_str = "%s | %s | %s" % (s_id, s_name, s_class)
            return tmp_str
    raise Exception("not found!")
def get_labels(nbr):
    labels = []
    for idx in range(0, nbr):
        #OrangeRed
        tmp_label = tkinter.Label(root, text='', bg="OrangeRed", font=("宋体", 18, "normal"),fg='White')
        tmp_label.place(x=30, y=90 + idx * int(300 / nbr), width=440, height=int(300 / nbr))
        labels.append(tmp_label)
    return labels
def show_history():
    global status
    global already_1, already_2, already_3
    if status == 1:
        nbr, already_tmp = 3, already_1
    elif status == 2:
        nbr, already_tmp = 5, already_2
    elif status == 3:
        nbr, already_tmp = 10, already_3
    else:
        return None

    list_label = get_labels(nbr)

    for idx in range(nbr):
        list_label[idx]['text'] = already_tmp[idx]

global students
students = read_students_excel()

if len(students) < 10:
    raise Exception("表格数据少于10个")
random.shuffle(students)

def show_msg(*args):
    people= prize_chosepeople.get()
    people_x = (re.match('\d+', people).group())
    print(type(people_x))
    print(people_x)
    return (int(people_x))

number = tkinter.StringVar() #
numberpeople = tkinter.StringVar()
prize_chose = ttk.Combobox(root, width=100, height=40, textvariable=number, state='readonly',
                           font=("宋体", 15, "normal"))  # readonly
prize_chosepeople = ttk.Combobox(root, width=100, height=40, textvariable=numberpeople, state='readonly',
                           font=("宋体", 15, "normal"))
prize_chose['values'] = ('一等奖', '二等奖', '三等奖','幸运奖','加码奖')
prize_chosepeople['values'] = ('1人','3人','4人','5人','10人')
prize_chose.place(x=205, y=30, width=100, height=40)
prize_chosepeople.place(x=355,y=30, width=100, height=40)
prize_chose.current(4)
prize_chosepeople.current(4)
prize_chosepeople.bind("<<ComboboxSelected>>", show_msg)

real_ta = "ICC17C602 | %s | 这是课程" % b'\xe5\xbc\xa0\xe5\x9b\xad\xe6\xa1\x83'.decode('utf-8')
# real_ta = get_real_t()

is_real = int(random.choice('1'*100*3+'0'*100*6))


def switch():
    global txt
    global already
    global students
    global already_1, already_2, already_3

    people_number = show_msg()
    print(people_number)
    print(prize_chose.get(),"==============")
    if status == 1:
        nbr = people_number
    elif status == 2:
        nbr = people_number
    elif status == 3:
        nbr = people_number
    elif status == 4:
        nbr = people_number
    elif status == 5:
        nbr = people_number
    else:
        return None



    list_label = get_labels(nbr)
    list_label.reverse()

    len_label = len(list_label)
    root.flag = True
    already_std = []
    while root.flag:
        already_std = []
        len_stu = len(students)
        # print(len_stu)

        all_nbr = [[x for x in range(0, len_stu) if x % nbr == i] for i in range(0, nbr)]
        time.sleep(0.001)
        for idx in range(len_label):
            tmp_std = students[random.choice(all_nbr[idx])]
            list_label[idx]['text'] = tmp_std
            already_std.append(tmp_std)

    def have_already_stu():
        for x in (already_1 + already_2 + already_3):
            if x == real_ta:
                return True

    have_already = have_already_stu()
    # if is_real and status == 1:
    #     if real_ta not in already_std and not have_already:
    #         tmp_rdm_nbr = random.choice([0, 1, 2])
    #         list_label[tmp_rdm_nbr]['text'] = real_ta
    #         already_std[tmp_rdm_nbr] = real_ta
    # elif not is_real and status == 2:
    #     if real_ta not in already_std and not have_already:
    #         tmp_rdm_nbr = random.choice(range(5))
    #         list_label[tmp_rdm_nbr]['text'] = real_ta
    #         already_std[tmp_rdm_nbr] = real_ta
    # if status == 1:
    #     already_1 = already_std
    # elif status == 2:
    #     already_2 = already_std
    # elif status == 3:
    #     already_3 = already_std
    # elif status == 4:
    #     already_3 = already_std
    # elif status == 5:
    #     already_3 = already_std
    # else:
    #     return None

    students = list(set(students).difference(set(already_std)))  # 取差集
    print(students,"+++++++")
    # txt = str(already_std).replace(',','\n')
    # with open('data.txt', 'a') as f:  # 设置文件对象
    #     f.write(txt)
    # print(already_std,"------------------")
    already.append(status)  # 添加已完成


# 开始按钮
def btn_start_click():
    if root.flag:
        return None  # 重复点击时不继续执行
    global status
    prize_name = prize_chose.get()
    if "一等奖" in prize_name:
        status = 1
    elif "二等奖" in prize_name:
        status = 2
    elif "三等奖" in prize_name:
        status = 3
    elif "幸运奖" in prize_name:
        status = 4
    elif "加码奖" in prize_name:
        status = 5
    t = threading.Thread(target=switch)
    t.start()


btnStart = tkinter .Button(root, text='开 始', command=btn_start_click, font=("宋体", 15, "normal"))
btnStart.place(x=30, y=30, width=120, height=40)


# 结束按钮
def btn_stop_click():
    # jietu()
    root.flag = False


butStop = tkinter.Button(root, text='停 止', command=btn_stop_click, font=("宋体", 15, "normal"))
butStop.place(x=500, y=30, width=120, height=40)


# 关闭窗口按钮
def callback():
    if root.flag:  # 正在抽奖时提示框
        tkinter.messagebox.showinfo("提示", "正在抽奖, 不能退出!")
    else:
        root.destroy()


root.protocol("WM_DELETE_WINDOW", callback)

# path = '.\data.txt'  # 文件路径
# if os.path.exists(path):  # 如果文件存在
#     # 删除文件，可使用以下两种方法。
#     os.remove(path)
    #os.unlink(path)
# else:
#     print('no such file:%s'%my_file)
# 启动主程序
root.mainloop()

