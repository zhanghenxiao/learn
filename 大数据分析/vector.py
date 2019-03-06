# -*- coding: utf-8 -*-
# @File    : vector.py
# @Date    : 2019-01-23
# @Author  : Zhang.Cookie

import numpy as np
#数组（arange,,array），几维
"""
c = np.array(['1','2','3'],dtype= int)
w = np.array([(np.arange(1,10,2)),(np.arange(11,20,2))])
print(c.dtype)
print(c.shape)
print(w.shape) #查看属性是几维

a = np.array([('abc',[1,2,3])],dtype= 'U3,3i4')   #dtype 指定类型
print(a[0]['f0'],a[0]['f1'][0])
b = np.array([('abc',[1,2,3])],dtype=[('name',np.str_,3),('age',np.int32,3)])
print(b[0]['name'],b[0]['age'][0])
c = np.array([('abc',[1,2,3])],dtype=[('name',np.str_,3),('age',np.int32,3)])
print(b[0]['name'],b[0]['age'][0])
#大端字节序 ，小端字节序
#np.str_ = u1 ;np.int = i1
# d = np.array([0x1234],dtype=('>u2',{'lo':('u1',0),'hi':('u1',1)})) #有待研究
# print('{:x}',format(d[0]))
# print('{:x} {:x}',format(d['lo'][0],d['hi'][0]))
"""
#切片
"""
e = np.array(np.arange(10))
print(e[::-1],e[:3],e[::2]) #[9 8 7 6 5 4 3 2 1 0] ,[0 1 2] ,[0 2 4 6 8]
f = np.arange(1,25).reshape(2,3,4)
print(f)
print(f[:,0,0]) # : 表示所有页
print(f[...,1],f[1,...,1]) # .... 表示从头到尾
"""
#改变维度,
# 视图数组.reshape,racel(换成一维)，flatten副本（所有都会新建）,就地变维 shape,resize,视图转置至少是二维transpose
print(type(np.arange(10)))
print(type(np.array([1,2])))
a = np.arange(10)
#组合与拆分，垂直组合vstack



# ll = [1,2,3]
# # ll.remove(1)
# # print(ll)
