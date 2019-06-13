# -*- coding: utf-8 -*-
# @File    : 类方法.py
# @Date    : 2019-03-14
# @Author  : Zhang.Cookie

#classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，
# 可以来调用类的属性，类的方法，实例化对象等。
#self 是实例  cls是单列  源至冯诺依曼结构 查看图
"""
class A(object):
    bar = 1
    def func1(self):
        print('foo')
    @classmethod
    def func2(cls):
        print('func2')
        print(cls.bar)  #直接调用类的属性
        cls().func1()  #直接调用类的方法
    @staticmethod
    def func3():
        print("func3")

a = A()
a.func1()
A.func2()
A.func3()     #静态方法无需实例化
A().func3()   #也可以实例化后调用
"""
# class test(object):
#     def __init__(self,w,lst,):
#         self.w = w
#         self.lst = lst
#     @classmethod
#     def onestr(cls,e):
#         w = e.split()
#         return cls(w,2)
# t = test.onestr("12 3")
# print(t.w)

class test(object):
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def study(self,study_name):
        print("%s正在学习%s"%(self.name,study_name))
    @staticmethod
    def st():
        print("1000")
    @classmethod
    def cl(cls):
        print("cl")
# w  = test("张先生",20)
test.st()
test.cl()

























