# -*- coding: utf-8 -*-
# @File    : 2用pands代替excel.py
# @Date    : 2019-05-23
# @Author  : Zhang.Cookiee
#https://www.echartsjs.com/index.html 官方文档
import pandas as pd
import numpy as np

# a  = '123条'
# print(a.split('1'))
# b = '123 条点评'
# print(b.split('条')[-1])

def two():
    df = pd.read_excel('./2.xls')  #获取excel
    print(df.columns)  #得到特征
    print(df.values)   #得到值
    # print(df['price'])  #列索引
    # print(df[['price','name']]) #多列索引
    # print(df.iloc[:5])  #行索引  特征筛选，df.loc[]
    # print(df[df['price']>130]['price'].mean())   #布尔类型索引 > 130 ,均值
    # print((df[df['price']>130])&([df['price']>1]))  #可双重条件（暂未成功）
    # print(df['price'].sum())  #和

    #pandas 套路,创建数据，分组，去重。替换
    # data = {'name':['a','b','c'],
    #         'age':[14,15,15],
    #         'gender':['m','m','w']
    # }
    # dff = pd.SparseDataFrame(data)
    # # print(dff)
    # #创建的第二种方式
    # ff = pd.DataFrame({'A':['foo','bar','bar','foo','bar','bar','bar','bar'],
    #                    'B':['one','two','there','four','two','there','four','there'],
    #                    'C': np.random.randn(8),
    #                    'D': np.random.randn(8)
    #                    })
    # print(ff)
    # print(ff.groupby(by='B').mean())
    # print(ff.groupby(by='B')['C'].mean())

    # print(df,"=========")
    # df1 = df[df['comment'].str.contains('条')] #筛选excel，comment列中筛选带有'条'的数据
    # print(df1,"**********")
    # test= df['comment'].str.split('条').str[0] #以'条'分割
    # # test = test.astype('int')  #转换数据类型 int
    # print(test)
    # test.to_excel("./2_1") #导出到excel
#two()


import os

path1=os.path.abspath('.')   #表示当前所处的文件夹的绝对路径
path2=os.path.abspath('..')  #表示当前所处的文件夹上一级文件夹的绝对路径

def read():
    df = pd.read_excel('../Autoit_work/iv.xlsx')
    print(df['Blurr\nEliteBook 1040 G5'])
    # print(df.values)
    # print(df[['price','name']]) #多列索引
    # print(df.iloc[:5])  #行索引  特征筛选，df.loc[]
    # print(df[df['price']>130]['price'].mean())   #布尔类型索引 > 130 ,均值
read()




