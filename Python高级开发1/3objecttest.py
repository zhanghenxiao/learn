#1-260 ---1-276
#封装（-）
#面向对象详解self
# class test:
#     def one(self,w):
#         print(w,self) #self是传入当前对象，python里面自行处理
# # #创建对象，实例
# t = test()
# print(t)
# t.one(100)
# t1 = test()
# print(t1)
# t1.one(100)
#继承,多继承（二）
# class test(): #父类
#     def chi(self): #基类
#         print(self.name + "吃")
#     def he(self):
#         print(self.name + "喝" )
# class test1():
#     def piao(self):
#         print(self.name + "漂")
# class cat(test,test1): #子类继承所有基类
#     def __init__(self,name):
#         self.name = name
#     def jiao(self): #派生类
#         print(self.name + "汪")
# #优先级:自己,左边,右边
# c = cat("alex")
# c.chi()
# c.he()
# c.piao()
#多态 （三）
#重载：函数名相同，参数不同
#重写：派生类中重新实现基类中得方法
# class test():
#     def one(self):
#         pass
#     def one(self,nice): #重载
#         pass
#代码级接口（必须实现，起约束作用）,业务接口
# iterface ifather()
#     def f1():pass
#     def f2():pass
#1-277
# - .反射：以字符串的形式去对象（模块）中操作成员
#getattr()
#__import__("lib.com",fromlist=True)
# 面向对象：封装,__init__ ,构造方法
#1-278
#多继承易错点,如何查看源码(代码的起始)
# class a:
#     def bar(self):
#         print("BAR") ###
#         self.f1()  ### c
# class b(a):
#     def f1(self):
#         print("b")
# class c(b):
#     def f1(self):
#         print("c") ### c
# class d(c,b):
#     pass
# dd = d() #执行构造方法
# dd.bar()
# 1-279
#执行父类（基类）的构造方法
#推荐使用super()
# class dog:
#     def __init__(self):
#         print("dog 构造方法")
#         self.ty = "小狗"
# class cat(dog):
#     def __init__(self):
#         print("cat 构造方法")
#         self.n = "小猫"
#         #super(cat,self).__init__()  #调用基类的构造方法一
#         #dog.__init__(self)  #调用基类的构造方法二
# c = cat()
# print(c.__dict__)
#1-280 ----- 1-282
# 源码分析
# 1-283 -------- 2-17
#利用反射查看对象成员归属
# class test:
#      #静态字段 在类中，每个对象都有一份
#     country = "china"
#     def __init__(self,name):
#           #普通字段,在对象中
#         self.name = name
#        #普通方法,在类中
#     def show(self):
#         pass
#     @staticmethod
#     def xo(j,k):  #静态方法无self可无参数,存在的意义不需要创建对象
#    #def xx():
#         print(j,k)
#     @classmethod  #类方法
#     def xxoo(cls):
#         print(100,cls)
#     @property  #特性：不能加参数，访问时不需要括号，将方法伪造成一段字段
#     def end(self):
#         temp = "%s"%self.name
#         return temp
#     @end.setter #特性需加参数规范,设置参数
#     def end(self,value):
#         print(value + 888)
# #反射以字符串的形式去对象操作成员
# #反射即可找对象也可以找类的成员
# #通过类访问的有：静态字段,静态方法,类方法
# #通过对象访问的有：普通字段，普通方法（类的方法），特性
# #快速判断，类执行，对象执行
# #有self对象调用，无self类调用
# t = test('alex')
# # r = hasattr(t,'name')
# # print(r)
# # print(test.country)
# # test.xo(1,2)
# # test.xxoo()
# print(t.end)
# t.end = 123
#2-18 --- #2-20
#成员修饰符
#私有 只能自己使用
# class foo():
#     xo = "xo"
#     _xxoo = "xxoo"    #私有静态字段
#     def __init__(self):
#         self._name = 'alex'
#     def say(self):
#         print(foo._xxoo) #私有静态字段调用
#         print(self._xxoo) #私有静态字段调用
#         foo.__test(self) #私有普通方法调用
#         self.__test()  #私有普通方法调用
#         print(self)
#     def __test(self):
#         print("__test")
# f = foo()
# print(f)
# f.say()

#开始针对学习---------
#2-27 异常处理
# inp = input('请输入;')
# try:
#     print(int(inp))
#     print('1')
# except Exception as e:  #万能接受错误类型
#     print(2)
# else:
#     print(3)
# finally:
#     print(4)
# assert 1==2   #断言
# test = "1","2","3"
# cc = ''.join(test)
# print(cc)


#单列模式 此处需要重温
#2-45 --- 2-61
#socket模块 网络编程,IO多路复用

#2-75 线程，进程，协程
#线程：
#优点：共享内存，IO操作时候，创造并发操作
#缺点：抢占资源
#进程：
#优点：同时利用多个CPU,能够进行多个操作
#缺点：h耗费资源（重新开辟内存空间）
#进程不是越多越好，cpu个数=进程个数；线程也不是越多越好
#计算机中执行任务的最小单元：线程
# IO操作利用CPU
# GIL全局解释器锁
# IO密集型(不用CPU)：多线程
# 计算密集型(用CPU)：多进程






































