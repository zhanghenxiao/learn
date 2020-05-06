# -*- coding: utf-8 -*-
# @File    : 内置函数.py
# @Date    : 2020-01-02
# @Author  : Zhang.Cookie

# getattr()
# class A(object):
#         value =  1
# a = A()
# print(getattr(a,'value'))

def test(yy=True, **kwargs):
    test_value = kwargs.get("tw", 2)
    testa = kwargs.get("cc", None)
    print(test_value, testa)
    dic = {
        "f5": "",
        "f6": "<",
        "f7": ">",
    }

    # if testa is dic["f"]


test(cc="f6")
