# -*- coding: utf-8 -*-
# @File    : cls_sta.py
# @Date    : 2019-12-24
# @Author  : Zhang.Cookie

class tt(object):
    def __init__(self,year):
        self.year =year
    def ttone(self):
        print(self.year)
    def tttwo(self):
        print("tttwo" +self.year)
    def __call__(self, *args, **kwargs):
        self.tttwo()

class test(tt):
    def __init__(self,name):
        self.name = name
    def one(self,name):
        print(self.name)
    @classmethod
    def cla(cls):
        print("cla")
    @staticmethod
    def sta():
        print(sta)
    # def __call__(self, *args, **kwargs):
    #     self.cla()
    #     self.tttwo()

if __name__ == '__main__':
    tt = tt(22)
    test = test("cookie")
    # test()
    tt()