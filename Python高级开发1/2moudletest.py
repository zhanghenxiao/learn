#https://www.cnblogs.com/jyfootprint/p/9409909.html
import sys
import os
import hashlib
import re
import requests
import json
import xml
import configparser
import shutil
import zipfile
import subprocess
import logging


# 1-204-----1-210
#模块导入
# print(sys.path)
# print(os.stat("c:\Testimage"))
#加密
# hash = hashlib.md5()
# hash.update(bytes("123",encoding='utf-8'))
# print(hash.hexdigest())
#加密实现登录和注册
# def md(a):
#     hash = hashlib.md5()
#     hash.update(bytes(pwd,encoding='utf-8'))
#     print(type(hash.hexdigest()))
#     return hash.hexdigest()
#
# def save(user,pwd): #进行保存
#     with open("test","w+",encoding='utf-8') as f:
#         temp = user + "||" + md(pwd)
#         print(type(temp))
#         f.write(temp)
#         f.close()
# # def login(user,pwd):
# #     with open("test","r+",encoding='utf-8') as f :
# #         for lit in f:
# #             u,p = lit.strip().split("||")  # strip去空格，split按||分割
# #             if u == user and p == md(pwd):
# #                 return True
# # i = input("1,登陆；2，注册") #
# # print(type(i))
# # if i == "2":
#     user = input("用户名:")
#     pwd = input("密码:")
#     save(user,pwd)  #跳转保存函数
# elif i== "1":
#     user = input("用户名:")
#     pwd = input("密码:")
#     r = login(user,pwd) # 跳转登陆函数
#     if r:
#         print("登陆成功")
#     else:
#         print("登陆失败")
#格式化
# %[(name)][flags][width].[precision]typecode
#s  = "this  name is %s age %d"%("zhang",18 ) #this  name is zhang age 18
#s  = "this  name is %(n1)s age %(n2)d"%{"n1":"zhang","n2":18}   #[(name)] ,this  name is zhang age 18
#s  = "this  name is %-10s age %d"%("zhang",18 ) #[flags],(+，-)左对齐，右对齐，[width]10长度占位符
# s = "i am %.3f asd" %1.2
# print(s)
#132 1254 9073

# 1-210
#format

#1-211-----1-214
#模块 json,pickele,xml,configparse,logging
# print(vars())
# """
#     "这是py文件的注释"
# """
# print(__doc__)
# print(__file__) #本身自己得路劲
# print(__package__) #本身的目录
# print(__name__)  #__main__
#得到当前文件的上一级文件名
# print(__file__) #C:/Users/succful/Desktop/opencvStudy/Python高级开发1/moudletest.py
# print(os.path.dirname(__file__)) #C:/Users/succful/Desktop/opencvStudy/Python高级开发1
# a = "c:"
# b = "\ test"
# print(os.path.join(a,b)) #拼接路劲
#1-215----1-218
#网页上得到的全是str ,所以需要用json,json是一种格式
#json.loads用于dict list tuple形式的字符串，转换成相应的dict list tuple   ,,引号很重要
# s = "[1,2,34,5]"
# s1 = '{"n1":"one"}'
# test = json.loads(s1)
# print(test)
#json.dumps 将python基本类型，转换成字符串
# s = [1,2,34,5]
# test = json.dumps(s)
# print(test,type(test))
# json.dump(s,open("db","w"))  #转换成字符串写入文件中
# print(json.load(open("db","r"))) #读取文件转换成原来基本类型
#json 使用通用的数据类型

#1-221
#requests模块
# test = requests.get("https://mva.microsoft.com/")
# test.encoding = "utf-8"
# print(test.text)
#1-222
#xml模块
#检查QQ是否在线，#利用腾讯的接口
# test = requests.get("http://www.webxml.com.cn/webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=2497430769")
# test.encoding = "utf-8"
# result = test.text
# from xml.etree import ElementTree as ET
# node = ET.XML(result)
# if node.text== "Y":
#     print("在线")
# else
#     print("离线")

#1-223 --- 1-232
# from xml.etree import ElementTree as ET
# ET.XML()
# ET.parse() 解析
#tree.write 重写
#获取列车时刻表 加text--这个很重要
# test = requests.get("http://www.webxml.com.cn/webservices/TrainTimeWebService.asmx/getDetailInfoByTrainCode?TrainCode=K234&UserID=")
# test.encoding = "utf-8"
# cartime = test.text
# from xml.etree import ElementTree as ET
# root = ET.XML(cartime)
# root1 = ET.XML(open("first.xml","r",encoding="utf-8").read())
# print(root.tag,root.attrib)
# for a in root:
#     print(a.tag)
#     for b in a:
#         print(b.tag)
# for node in root.iter("TrainDetailInfo"): #TrainDetailInfo节点
#     print(node.find("TrainStation").text,node.find("ArriveTime").text,node.tag)
#XML 含有节点tag,属性attrib,文本text
# 修改并解析XML
# from xml.etree import ElementTree as ET
# tree = ET.parse("first.xml") #解析XML
# root = tree.getroot() #获取(根)顶层的节点
# print(type(root)) #Element类型
# print(root)
#print(dir(root)   #查看所有办法
# for node in root.iter("from"):
#     print(node.text)
#     new_from = str(node.text)+"thisistest"
#     node.text = new_from
#     #node.set('age',18) #xml加入属性 当时失败
# tree.write("first.xml") #把从内存修好好的文本写进xml
#二种方式创建节点
# son = root.makeelement("tt",{'kk':"vv"})
# root.append(son)
# s = son.makeelement("sunzi",{'kk':"123"}) #创建子节点
# son.append(s)
# tree.write("new.xml")
# a = ET.Element("one",{'kk':"vv"})
# b = ET.Element("two",{'kk':"vv"})
# root.append(a)
# a.append(b)
# tree.write("new.xml",short_empty_elements=False)
#1-239 ----- 1-240
#configparser模块,操作特定格式文件夹
# con = configparser.ConfigParser()
# con.read("configparser.txt",encoding='utf-8')
# test = con.sections() #返回所有节点名称
# print(test)
# te = con.options('zhang') #返回指定节点key值对
# print(te)
# con.add_section('addone') #增加
# con.write(open('configparser.txt','w'))
#1-241 ----- 1-242
#shutil模块，高级的文件,文件夹，压缩包处理模块，满足所有对文件夹的操作
# shutil.copy('configparser.txt','configparser2.txt') #copy文件夹
#zipfile模块，专注解压一百年。
#压缩
# z = zipfile.ZipFile('testzipfile.zip','w')  #'W'
# z.write('new.xml') #压缩
# z.write('db')
# z.close()
# 解压
# z = zipfile.ZipFile('testzipfile.zip','r')  #'r'
# z.extract('new.xml') #解压
# z.close()
# z.extractall() 解压所有文件
# print(z.namelist()) 得到所有安装包list
#1-243
#subprocess模块，用于执行系统命令
# s = subprocess.call('ipconfig')
#1-244 ---------1-245
#logging模块
# logging.error("sss")
#定义文件
# file = logging.FileHandler('testlogging.txt','a')
# fmt = logging.Formatter()
# file.setFormatter(fmt)
# #定义日志
# logger1 = logging.Logger('S1',level=logging.ERROR) #设置阀值40
# logger1.addHandler(file)
# #写日志
# logger1.critical('111111')
#1-246 --- 1-249
#生成器,debug模式调试
# def xrange(n):
#     start = 0
#     while  True:
#         if start > n:
#             return
#         yield start
#         start = 1
# obj叫做生成器,具有一种生成能力，第一次到yield终止，第二次进入从yield开始
# obj = xrange(5)
# 具有访问能力，迭代器
# n1 = obj.__next__()
# n2 = obj.__next__()
# n3 = obj.__next__()
# print(n1,n2,n3)
#1-254 ------1-260
#反射：根据字符串的形式去对象（某个模块）去操作成员
# inp = input("请输入模块名：")
# inp_fuc = input("请输入函数名")
# print(inp,type(inp))
# dd = __import__(inp) #通过字符串的形式，导入模块。
# getfunc = getattr(dd,inp_fuc) #通过字符串形式，去寻找模块中的函数
# getfunc() #并执行
# import test 等同 __import__('test')
# getfunc = getattr(test,'f1')
# getfunc()
# dd = hasattr(test,'f1') #通过字符串，判断test模块中是否有F1
# print(dd)
# setattr(test,'AGE',18) #在内存中设置
#思想：模块名/函数名
# inp = input("请输入测试函数和模块名：")#fanshe_moudle1/test
# getmodle,getfunc = inp.split('/')
# print(getmodle,getfunc)
# moudle = __import__(getmodle)
# if hasattr(moudle,getfunc):
#     print(1)
#     func = getattr(moudle,getfunc)
#     func()
#     #print(c)
# else:
#     print('404')
#c = __import__("s2",fromlist=True) #联系到类里面的方法是需要用到

s = 0
while s<5:
    print(s)
    s+=1












































