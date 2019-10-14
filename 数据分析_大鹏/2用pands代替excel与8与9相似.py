# -*- coding: utf-8 -*-
# @File    : 2用pands代替excel.py
# @Date    : 2019-05-23
# @Author  : Zhang.Cookiee
#https://www.echartsjs.com/index.html  echarts官方文档
#https://www.pypandas.cn/  pandsa中文官方文档
import pandas as pd
import matplotlib.pyplot as plt

# a  = '123条'
# print(a.split('1'))
# b = '123 条点评'
# print(b.split('条')[-1])

# 云词汇 https://wordart.com/create

def two():
    df = pd.read_excel('./2.xls')  #获取excel
    print(df.columns)  #得到特征
    #print(df.values)   #得到值
    print(df['price'])  #列索引
    # w = df['price']
    # w.plot(kind = 'bar',figsize = (12,5),grid=True)  #失败。。。。
    df = pd.Series([1,23,4])
    print(df)

    #参考    https: // segmentfault.com / a / 1190000018177573
    #print(df['key'].str.upper()) #把这列改成大写
    # print(df['key'].str.startswith('a'))  #判断起始是否为a
    #print(df['key'].tolist())    #输出到列表中
    # print(df[['price','name']]) #多列索引 同时输出键名
    #print(df.head(1),'head')  #获取第几条数据
    # print(df.iloc[:5])  #行索引  特征筛选，df.loc[]
    # print(df[df['price']>130]['price'].mean())   #布尔类型索引 > 130 ,均值
    # print((df[df['price']>130])&([df['price']>1]))  #可双重条件（暂未成功）
    # print(df['price'].sum())  #和
    #print(df.ix[:, ['商品名称', '价格']].values)   #会输出一个列表
    #df['数量'][df['商品名称'] == sale] -= int(cout)  #数量减去
    #pandas 套路,创建数据，分组，去重。替换  #注意创建时必须时列表
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
    # https://www.kesci.com/home/project/5cd2b2b2e2889b002bbd6e8b/code
    # 3、Pandas套路总结¶
		# 数据类型问题，series和dataframe
		# 去重.duplicated
		# 替换 .replace
		# 分组 .groupby
		# 合并  merge
two()


import os

path1=os.path.abspath('.')   #表示当前所处的文件夹的绝对路径
path2=os.path.abspath('..')  #表示当前所处的文件夹上一级文件夹的绝对路径




