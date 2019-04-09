# -*- coding: utf-8 -*-
# @File    : create_excel.py
# @Date    : 2019-04-01
# @Author  : Zhang.Cookie

import xlwt
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
workbook.save('Excel_test.xlsx')
