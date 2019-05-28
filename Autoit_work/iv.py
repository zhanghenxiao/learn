# -*- coding: utf-8 -*-
# @File    : iv.py
# @Date    : 2019-05-20
# @Author  : Zhang.Cookie

import xlrd

file = "iv.xlsx " #需要读取的文件
"""
def read_excel(platform,os,ostype,preinstall):

    wb = xlrd.open_workbook(filename=file)#打开文件
    #print(wb.sheet_names()) #获取所有表格名字  #[sheet1,sheet2,sheet3]
    sheet2 = wb.sheet_by_index(1)#通过索引获取表格  #[sheet2]

    #sheet2 = wb.sheet_by_name('CMIT NB SW')#通过名字获取表格
    # print(sheet2)
    #print(sheet2.name,sheet2.nrows,sheet2.ncols) #获取总的行，列数
    rows1 = sheet2.row_values(1)  # 获取所有平台
    rows0 = sheet2.row_values(0)  # 获取os
    platform_line = (rows1.index(platform))   #获取平台对应的列数
    os_line = (rows0.index(os))  # 获取平台对应的列数
    preinstall_line =(rows1.index(preinstall))
    # print(rows1.index(32.0),os_line)
    # #print(rows0.index('Win10 \nG'),'64.0')
    # print(rows0,rows1)

    four_list = []
    for i in range(2,415):  #通过行来获取整个列
        rows = sheet2.row_values(i)
        fourcols = (rows[4])
        four_list.append(fourcols)
    print(len(four_list))
    PLATFORM_Xlist = []   #对应平台需要测试的case
    for i in range(2,415):
        rows1 = sheet2.row_values(i)
        X_line = (rows1[platform_line])
        if 'X' in X_line:
            PLATFORM_Xlist.append(i)
    #print(len(PLATFORM_Xlist),PLATFORM_Xlist)

    os_creening = []
    for case in PLATFORM_Xlist:
        #print(four_list[case - 2])
        os_creening.append(four_list[case - 2])
    # print(len(os_creening))

    if ostype == '32.0':
        os_line = os_line -1
        print(os_line)
    elif ostype == '64.0':
        os_line =os_line
        print(os_line)
    OS_Xlist = []        # 对应os需要测试的case
    for i in range(2, 415):
        rows1 = sheet2.row_values(i)
        X_line = (rows1[(os_line -1)])
        if 'X' in X_line:
            OS_Xlist.append(i)
    #print(len(OS_Xlist),OS_Xlist)

    #platform_os = list(set(PLATFORM_Xlist).intersection(set(OS_Xlist)))  #得到plafrom 和 os 相交的case
    platform_os = list(set(OS_Xlist).intersection(set(PLATFORM_Xlist)))

    PREINSTALL_Xlist = []  # 对应preinstall需要测试的case
    for i in range(2, 415):
        rows1 = sheet2.row_values(i)
        X_line = (rows1[preinstall_line])
        if 'X' in X_line:
            PREINSTALL_Xlist.append(i)
    #print(len(PLATFORM_Xlist),PREINSTALL_Xlist)

    platform_os_preinstall = list(set(platform_os).intersection(set(PREINSTALL_Xlist)))
    #print(len(platform_os_preinstall),platform_os_preinstall)

    platform_case = []
    for case in PLATFORM_Xlist:
        platform_case.append(four_list[case - 2])
        #print(four_list[case - 2])
    print(len(platform_case))  #138   #1 .HP Jump Starts (MyHP) #2.HP lt4220 Snapdragon X12 LTE Drivers
    w = list(set(four_list).difference(set(platform_case)))
    print(len(w))

    os_case = []
    for case in OS_Xlist:
       os_case.append(four_list[case - 2])
    print(len(os_case))  # 294

    preinstall_case = []
    for case in PREINSTALL_Xlist:
        preinstall_case.append(four_list[case - 2])
    print(len(preinstall_case))  # 234

#read_excel(platform = 'Blurr\nEliteBook 1040 G5',os = "Win10\nRS5",ostype = '64.0',preinstall = 'Preinstall')
"""

def niubi_case(platform,os):
    wb = xlrd.open_workbook(filename=file)  # 打开文件
    sheet2 = wb.sheet_by_index(1)  # 通过索引获取表格  #[sheet2]
    rows1 = sheet2.row_values(0)  # 获取所有平台
    # print(rows1)
    # a = -1
    # dict1 = {}
    # for i in rows1:
    #     a += 1
    #     if a >= 6 :
    #         dict1[i] = a
    #     else:
    #         continue
    #print(dict1)
    # platform_line = (rows1.index(platform))
    # print(platform_line)

    c = []
    #yy = 42   #104  #rs5 32.0
    #yy = 43  #300  #rs5  64.0  去除所有筛选
    yy = 44  #290
    #yy = 45  #67
    #yy = 46   #196
    # for i in range(2,415):  #通过行来获取整个列
    #     # print(sheet2.row_values(i)[30])
    #     if "X" in str(sheet2.row_values(i)[yy]) or "x" in str(sheet2.row_values(i)[yy]):
    #         c .append(i)
    # print(len(c))
    os_line0 = (rows1.index(platform))   #获取os对应的列数
    os_vaule = str(sheet2.row_values(1)[os_line0])
    #print(os_line,os_vaule,'====')
    if "32.0" in os_vaule :
        print('--------------')
        # os_line = os_line
        if os == '32.0':
            os_line = os_line0
        if os == '64.0':
            os_line = os_line0 +1
    elif '64.0' in os_vaule:
        print("+++++++++")
        print(os,os_vaule)
        if os == '64.0':
            os_line = os_line0
        else:
            print("请输入正确的os信息")
    for i in range(2,415):  #通过行来获取整个列
        # print(sheet2.row_values(i)[30])
        if "X" in str(sheet2.row_values(i)[os_line]) or "x" in str(sheet2.row_values(i)[os_line]):
            c .append(i)
    print(len(c))
    print(os_line)
#
# niubi_case(platform = "Win10\nRS5",os = '32.0')
# niubi_case(platform = "Win10\nRS5",os = '64.0')
#
# niubi_case(platform = "Win10 \n19h1",os = '64.0')
# niubi_case(platform = "Win10\nIoT",os = '32.0')
# niubi_case(platform = "Win10\nIoT",os = '64.0')

def read_case(platform,os,ostype,preinstall):
    wb = xlrd.open_workbook(filename=file)#打开文件
    sheet2 = wb.sheet_by_index(1)#通过索引获取表格  #[sheet2]
    # print(sheet2.cell(0, 1).value)
    # print(sheet2.cell(1, 1).value)
    #print(sheet2.cell(130, 30).value)  #行，列
    # sheet2 = wb.sheet_by_name('CMIT NB SW')#通过名字获取表格
    # print(sheet2)
    #print(sheet2.name,sheet2.nrows,sheet2.ncols) #获取总的行，列数
    rows1 = sheet2.row_values(1)  # 获取所有平台
    rows0 = sheet2.row_values(0)  # 获取os
    platform_line = (rows1.index(platform))   #获取平台对应的列数
    os_line0 = (rows0.index(os))  # 获取平台对应的列数
    os_vaule = str(sheet2.row_values(1)[os_line0])
    preinstall_line =(rows1.index(preinstall))  #获取preinstall对应列数（目前是需+1）
    # print(os_line)
    # if ostype == '32.0':
    #     os_line = os_line
    # elif ostype == '64.0':
    #     os_line =os_line + 1
    #     print('64.0 索引%s'%os_line)

    if "32.0" in os_vaule :
        print('--------------')
        # os_line = os_line
        if ostype == '32.0':
            os_line = os_line0
        if ostype == '64.0':
            os_line = os_line0 +1
    elif '64.0' in os_vaule:
        # print("+++++++++")
        # print(os,os_vaule)
        if ostype == '64.0':
            os_line = os_line0
        else:
            print("请输入正确的os信息")

    four_list = []
    for i in range(2, 415):  # 通过行来获取整个列
        rows = sheet2.row_values(i)
        fourcols = (rows[4])
        four_list.append(fourcols)

    platformlist = []
    oslist = []
    preinstall_list = []
    for i in range(2,415):  #通过行来获取整个列
        # if "X" in str(sheet2.row_values(i)[os_line]) or "x" in str(sheet2.row_values(i)[os_line]):
        #     onelist.append(i)
        if ('X') in sheet2.cell(i,platform_line).value or ('x') in sheet2.cell(i,platform_line).value:  #获取打'x','X'测试行
            platformlist.append(i)
        if ('X') in sheet2.cell(i,os_line).value or ('x') in sheet2.cell(i,os_line).value:
            oslist.append(i)
        if ('X') in sheet2.cell(i,preinstall_line).value or ('x') in sheet2.cell(i,preinstall_line).value:
            preinstall_list.append(i)
    onelist = list(set(platformlist).intersection(set(oslist)))
    endlist = list(set(onelist).intersection(set(preinstall_list)))
    # print(len(endlist),endlist)
    case_list = []
    for case in endlist:
        #print(four_list[case - 2])
        case_list.append(four_list[case - 2])  # 以'x'索引遍历第四列，得到所需case
    # print(len(case_list),sorted(case_list))
    return sorted(case_list)
#read_case(platform = 'Blurr\nEliteBook 1040 G5',os = "Win10 \n19h1",ostype = '64.0',preinstall = 'Preinstall')

contorllist = {"2013 Bucket 3 HP Client Security Manager":"env.HP_Client_Security_Manager","HP Collaboration Keyboard":"env.HP_Collaboration_Keyboard","HP Connection Optimizer":"env.HP_Connection_Optimizer",
               "HP Documentation":"env.HP_Documentation","HP Mac Address Manager":"env:HP_Mac_Address_Manager","HP Notifications":"env:HP_Notifications",
               "HP Support Assistant":"evn.HP_Support_Assistant","HP Sure Run":"env.HP_Sure_Run","HP Sure Recover":"HP_Sure_Recover"}
class function():
    def contorl(self):
        print("=                   =======================")
    def system(self):   # 打开sav
        pass
fu = function()
fu.contorl()
def runcase():
    testcase = read_case(platform = 'Blurr\nEliteBook 1040 G5',os = "Win10 \n19h1",ostype = '64.0',preinstall = 'Preinstall')
    # print(testcase)
    print(type(testcase))
    for i in testcase:
        if i in contorllist:
            fu.contorl()
runcase()


# test = ['2013 Bucket 3 HP Client Security Manager', 'BCU FPR F10 Reset', 'Bing Search for IE11']
# a  = 'A'
# print(a.lower())
# incontest = ['HP Client Security Manager']
# def contorl(i):
#
#     pass
# def device(i):
#
#     pass
# for i in test:
#     print(i.lower())

# a = "2013 Bucket 3 HP Client Security Manager"
# for i in contorllist:
#     print(i.replace(' ','_'))
# if '' in str(a):
#     print()











