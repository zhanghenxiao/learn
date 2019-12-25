# -*- coding: utf-8 -*-
# @File    : fr.py
# @Date    : 2019-11-15
# @Author  : Zhang.Cookie

# def test(a,b: str = "b"):
#     print(a,b)
# test(a = "a",b = "w")

#异常处理（处理逻辑异常）
a = "1"
try:
    try:
        if a == 1:
            print(1)
    except:
        print(2)
except:
    print(3)
finally:
    print(4)

#python @property的用法及含义全面解析
class Test1(object):
    def __init__(self):
        self.width = 10
        self.height = 20
r = Test1()
print(r.width)
r.width = 200
print(r.width)
#实际使用中会产生一个严重的问题，__init__ 中定义的属性是可变的，
# 换句话说，是使用一个系统的所有开发人员在知道属性名的情况下，可以进行随意的更改(尽管可能是在无意识的情况下)，但这很容易造成严重的后果。

class Test2(object):
    @property
    def width(self):
        #变量名不与方法名重复
        return self.true_width
# s = Test2()
# s.width = 1000
# print(s.width)
# 此时，如果在外部想要给width重新直接赋值就会报AttributeError: can't set attribute的错误，这样就保证的属性的安全性。

class Test3(object):
    @property
    def width(self):
        #变量名不与方法名重复
        return self.true_width
    @width.setter  #可写
    # 与property定义的方法名要一致
    def width(self,input_width):
        self.true_width = input_width
there = Test3()
there.width = 1024
print(there.width)
# 总结一下 @ property提供了可读可写可删除的操作，如果像只读效果，就只需要定义 @ property就可以，不定义代表禁止其他操作

class pager(object):
    def __init__(self,page):
        self.page = page
        self.page_items = 10
    @property
    def start(self):
        val = (self.page - 1) * self.page_items
        return val
p = pager(20)  #京东分页
print(p.start)

class goods(object): # 经典类（一种访问方式） / 新式类（三种访问方式）
    @property
    def price(self):
        print('@property')
    @price.setter
    def price(self,value):
        print("@property",value)
    @price.deleter
    def price(self):
        print("@property.deleter")
g = goods()
g.price
g.price = 123  #执行 @price.setter 修饰的 price 方法，并将 123 赋值给方法的参数
del g.price    #执行deleter方法

#原价（Original_price），折扣(discount)
class Original_price(object):
    def __init__(self):
        self.Original_price  = 100
        self.discount = 0.8
    @property
    def price(self):
        new_price = self.Original_price * self.discount
        return new_price
    @price.setter
    def price(self,value):
        self.Original_price = value
    @price.deleter
    def price(self):
        del self.Original_price
o = Original_price()
print(o.price)  #获取商品价格
o.price = 200   #修改商品价格
print(o.price)  #删除商品原价
del o.price

# super() 函数用于调用下一个父类(超类)并返回该父类实例的方法。
# super 是用来解决多重继承问题的


















