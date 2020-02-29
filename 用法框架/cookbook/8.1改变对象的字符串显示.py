# -*- coding: utf-8 -*-
# @File    : 8.1改变对象的字符串显示.py
# @Date    : 2019-12-25
# @Author  : Zhang.Cookie


#格式化默认顺序  format
#格式化
"""
def cool()
    print("{},{}".format("hello","1"))
    #格式化指定顺序
    print("{1},{1}".format("hello","world"))
    #格式化列表使用
    person = {"name":"cookie","age":23}
    print("name is {name},age is {age}".format(**person))
cool
"""

#8.1改变对象的字符串显示  def __str__(self):
"""
class pair():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #返回对象的描述信息，方便开发者查看对象信息
    def __str__(self):
        return ("name is {},age is {}".format(self.name,self.age))
        # return '({0.x!s}, {0.y!s})'.format(self)

p = pair("sheng",23)
print(p)
print('p is {0}'.format(p))
"""

#8.4 创建大量对象时节省内存方法  理解为限制属性绑定  python __slots__
#使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的：
"""
class student():
    pass
 
s = student()
s.name = "cc" #动态给实例绑定一个属性，绑定属性
s.age = 23
s.gender = "gender"
print(s.name,s.age,s.gender)


class trueslots():
    __slots__ = ['name','gender']
    pass

t = trueslots()
t.name = "cookie"
t.gender = "gender"
t.age = "age"  #限制给实列绑定属性
print(t.name,t.gender,t.age)
"""

# 私有方法的使用   类的内部调用  满足及条件即可调用
"""
class a():
    def test1(self):
        print("普通方法test1")
    def __test2(self):
        print("私有方法")
        # self.__test2()
    def test2(self,age):
        if age > 23:
            self.__test2()  #内部使用满足条件时  执行内部私用方法
        else:
            print("年纪小余23")
a = a()
a.__test2() #需内部调用
a.test2(50)
"""

#私有属性 也不能外部访问  只能内部调用
"""
class student(object):
    def __init__(self,name):
        self.__name = name

    def getname(self,newname):
        if (len(newname)>5):
            return self.__name
        else:
            return "字符长度不足5"

stu = student("ok")
print(stu.getname('cookiee'))
"""

#8.6创建可管理的属性 @property装饰器就是负责把一个方法变成属性调用
"""
class student(object):
    @property
    def get_width(self):
        return self._get_width
    @get_width.setter
    def get_width(self,width:int):
        if not isinstance(width,int):
            raise ValueError('width is not int' )
        if width < 0 or width >100:
            raise ValueError('width qujian daxiao')
        self._get_width = width
    @property
    def get_height(self):
        return self._get_height
    @get_height.setter
    def get_height(self,height):
        if not isinstance(height,int):
            raise ValueError('width is not int' )
    @property
    def resolution(self):
        return 200-self._get_width

stu = student()
stu.get_width = 100
print(stu.resolution)
"""

# @property 廖雪峰
"""
# class school(object):
#     @property
#     def sorce(self):
#         return self._sorce  #需与方法名有区别
#     @sorce.setter
#     def sorce(self,value):
#         if not isinstance(value,int):
#             raise ("请输入整数")
#         if value<0 or value>100:
#             raise ("请输入整数0-100间")
#         self._sorce = value #需定义返回值
# s =school()
# s.sorce = 80
# print(s.sorce)
"""

#闭包
"""
def print_msg():
    msg = "I'm closure"

    # printer是嵌套函数
    def printer():
        print(msg)

    return printer
# 这里获得的就是一个闭包
closure = print_msg()
# 输出 I'm closure
closure()
"""

#8.7调用父类方法  你想在子类中调用父类的某个已经被覆盖的方法。(覆盖得方法)可以使用 super() 函数
"""
# class A(object):
#     def ac(self):
#         print("ac")
# class B(A):
#     def ac(self):
#         print("dc")
#         super().ac() #调用父类已重新得方法
# b = B()
# b.ac()
"""

#确保父类被正确的初始化super() 函数
"""
class A():
    def __init__(self):
        self.x =  1
class B(A):
    def __init__(self):
        super().__init__() #不添加这个无法使用对象 x
        self.y = 2
b = B()
print(b.x,b.y)
"""

#这个MRO列表的构造是通过一个C3线性化算法来实现,a = B（） B..__mro__
"""
class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')

class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')

class C(A,B):
    def __init__(self):
        super().__init__()  # Only one call to super() here
        print('C.__init__')
c = C()
print(C.__mro__)
"""

#构造函数的使用方法
"""
class A():
    def __init__(self,name):
        print(3)
        self.name = name
        self.test1()
        self.test2()
    def test1(self):
        print("test1")
        print(self.name)
    def test2(self):
        print("test2")

a = A(name='cookie')
a
"""

#抽象类 abc 只能被继承，不能实例化  http://www.imooc.com/article/74245
"""
import abc
class MM(metaclass=abc.ABCMeta): #只能被继承，不能被实例化
    @abc.abstractmethod  ##加完这个方法下面子类必须有这个方法，否则报错
    def run(self):
        pass
    @abc.abstractmethod
    def eat(self):
        pass
class people(MM):
    def run(self):  #如上面抽象类定义了此方法，下面子类必须要有此方法
        print("this is people run")
    def eat(self):
        print("this is people eat")
class dog(people):
    def run(self):
        print("this is dog run")

peo = people()
peo.eat()
d = dog()
d.run()
"""

























