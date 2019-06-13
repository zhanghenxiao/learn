# -*- coding: utf-8 -*-
# @File    : 11可视化工具Tableau.py
# @Date    : 2019-05-30
# @Author  : Zhang.Cookie
#数据来源  http://info.2012.163.com/athlete/list/

import requests
from bs4 import BeautifulSoup

url = "http://info.2012.163.com/athlete/list_alphabet/A.html"  #数据无法采集。。。。
s = "http://info.2012.163.com/athlete/list/"
#htmls = list(map(chr, range(ord('A'), ord('B') + 1)))
urlslist = [chr(i) for i in range(65,91)]  #通过ASCII生成大写字母列表

# urlslist = []
# def urls():
#     for i in htmls:
#         urlslist.append("http://info.2012.163.com/athlete/list_alphabet/%s.html"%i)
# urls()
# urlslist = urlslist[:2]

def data():
    # for i in urlslist:
        res = requests.get(s)
        soups = BeautifulSoup(res.text,'lxml',from_encoding='utf-8')
        print(soups.find('title').text)
data()








