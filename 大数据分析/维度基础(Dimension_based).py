# -*- coding: utf-8 -*-

# @File    : testnumpy.py
# @Date    : 2019-01-18
# @Author  : Zhang.Cookie
#numpy是一个处理数组得强大模块，也是其它数据分析模块（pandas和scipy）得核心
import numpy as np
import matplotlib.pyplot as mp

# 详细完整请查看笔记day01.docx

"""
#一维数组得创建,可以是list,tuple构成
ls2 = np.arange(10) #有规律得一维数组
list(ls2)
print(list(ls2))
print(type(ls2)) #这是一个一维数组

arr1 = np.array((1,4,5,9)) #人为输入，需用array()函数创建

#二维数组得创建，就是列表套列表或元组套
arr3 = np.array((((1,3,5),(2,4,8),(6,7,8),(1,1,2))))
print(arr3)
"""
# print(np.ones(3)) #返回一维全为0数组
# print(np.ones([3,4]))#二维 1
# print(np.zeros(3)) #一维 0
# print(np.zeros([3,4])) #二维 0

#有关数组属性和函数
"""
arr3  = np.array(([1,2,3],[2,6,7]))
print(arr3)
print(arr3.shape) #shape返回数组行和列
print(arr3.dtype) #dtype 数据类型
print(arr3.dtype.str)
a = arr3.ravel()  #使多维降为一维
print(a)
print(arr3.size)  #元素数
print(arr3.itemsize) #元素字节数
print(arr3.flat)
"""
























