#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xlrd
from datetime import date,datetime

file = 'test.xlsx' #需要读取的文件

def read_excel():

    wb = xlrd.open_workbook(filename=file)#打开文件
    print(wb.sheet_names()) #获取所有表格名字  #[sheet1,sheet2,sheet3]

    sheet1 = wb.sheet_by_index(0)#通过索引获取表格  #[sheet2]
    #sheet2 = wb.sheet_by_name('班级')#通过名字获取表格
    #print(sheet1)
    #print(sheet1.name,sheet1.nrows,sheet1.ncols) #获取总的行，列数
    rows = sheet1.row_values(1)#获取行内容
    cols = sheet1.col_values(1)#获取列内容
    print(rows)
    print(cols)
    # print(sheet1.cell(1,0).value)#获取表格里的内容，三种方式
    # print(sheet1.cell_value(1,0))
    # print(sheet1.row(1)[0].value)
    # cla = sheet1.row_values(0)
    # i = cla.index('姓名')
    # n = cla.index('课别')
    # d = cla.index('工号')
    # print(cla)
    # print(i,n,d)
    # print(type(i))
    # cols = sheet1.col_values(i)  # 获取列内容
    # print(cols)
    # for x in range(sheet1.nrows):
        #print(sheet1.cell(x, i).value)
        # a = (sheet1.cell(x, i).value)
        # print(sheet1.cell(x, n).value)
        # print(sheet1.cell(x, d).value)

read_excel()
    # rows = sheet1.row_values(1)#获取行内容
    # cols = sheet1.col_values(2)#获取列内容
    # print(rows)
    # print(cols)
    # print(sheet1.cell(1,0).value)#获取表格里的内容，三种方式
    # print(sheet1.cell_value(1,0))
    # print(sheet1.row(1)[0].value)
