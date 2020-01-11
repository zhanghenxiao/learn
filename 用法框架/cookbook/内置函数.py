# -*- coding: utf-8 -*-
# @File    : 内置函数.py
# @Date    : 2020-01-02
# @Author  : Zhang.Cookie

#getattr()
class A(object):
        value =  1
a = A()
print(getattr(a,'value'))