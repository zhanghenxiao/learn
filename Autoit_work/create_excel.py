# -*- coding: utf-8 -*-
# @File    : create_excel.py
# @Date    : 2019-04-01
# @Author  : Zhang.Cookie

import xlwt,datetime,xlrd
import xlutils.copy,os,sys

"""
# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding = 'utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('My Worksheet')
# 写入excel
# 参数对应 行, 列, 值
worksheet.write(0,0, label = 'test case')
worksheet.write(0,1, label = 'expected results')
worksheet.write(0,2, label = 'actual results')

# 保存
workbook.save('Excel_test1.xlsx')
"""
#设置字体
"""
workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('My Worksheet')
style = xlwt.XFStyle() # 初始化样式
font = xlwt.Font() # 为样式创建字体
font.name = 'Times New Roman'
font.bold = True # 黑体
font.underline = True # 下划线
font.italic = True # 斜体字
style.font = font # 设定样式
worksheet.write(0, 0, 'Unformatted value') # 不带样式的写入
worksheet.write(1, 0, 'Formatted value', style) # 带样式的写入
workbook.save('formatting.xls') # 保存文件
"""
# 设置单元格宽度
"""
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
worksheet.write(0, 0,'My Cell Contents')
worksheet.col(0).width = 6553
worksheet.row(0).height = 1000000
workbook.save('cell_width.xls')

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
style = xlwt.XFStyle()
style.num_format_str = 'M/D/YY' # Other options: D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss, M/D/YY h:mm, mm:ss, [h]:mm:ss, mm:ss.0
worksheet.write(0, 0, datetime.datetime.now(), style)
workbook.save('Excel_Workbook.xls')
"""

open('ttt.xls','w+')  #创建任何类型文件
#实现功能往excel写数据并保存之前数据
filename = "readline.xls"
def readline():
    wb = xlrd.open_workbook(filename,formatting_info=True)  #打开excel，保留文件格式
    sheet1 = wb.sheet_by_index(0)  #获取第一张表
    nrows = sheet1.nrows  #获取总行数
    ncols = sheet1.ncols
    return nrows
def write(labbel,labbeltwo,labbelthere):
    data = xlrd.open_workbook(filename)
    ws = xlutils.copy.copy(data) #复制之前表里存在的数据
    table=ws.get_sheet(0)
    nownrows = readline()
    table.write(nownrows, 0, labbel )  #最后一行追加数据
    print(labbel)
    table.write(nownrows, 1, labbeltwo)
    table.write(nownrows, 2, labbelthere)
    ws.save(filename)  #保存的有旧数据和新数据
i = 0
while i <20:
    write("Prepare the Client unit for testing according to the configuration above",
      "For Thunderbot testThe exptected result, Please refer the TBT platform matrix",
      "pass")
    i+= 1
# print(os.getcwd())
# os.makedirs("test.xlsx")

def creat():
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet')
    # 写入excel
    # 参数对应 行, 列, 值
    worksheet.write(0, 0, label='test case')
    worksheet.write(0, 1, label='expected results')
    worksheet.write(0, 2, label='actual results')
    # 保存
    workbook.save(filename)
creat()




























