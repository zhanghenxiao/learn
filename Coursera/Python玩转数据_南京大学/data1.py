# -*- coding: utf-8 -*-
# @File    : show_np.py
# @Date    : 2019-06-27
# @Author  : Zhang.Cookie

import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import lxml

def shows():
    t = np.arange(0,4,0.1)
    plt.plot(t,t+t,t**2)
    plt.show()

    print(5%3)  #取余  2
    r = lambda x : x + x
    t = lambda x,y : x + y
    print(r(3),t(6,6))


#指针问题 f.seek(0)或f.seek(0,0) ,f.seek(50,1)
def read1():
    with open("test.txt") as f:
        p1 = f.read(5)
        p2 = f.read()
        # f.seek(0,0)
        p3 = f.readlines()
    print(p3)
    # print(p1)
    # print(p2)
#读取test.txt 新增数据到 add_test
def read3():
    with open('test.txt','r') as f:
        names = f.readlines()
        for i in range(0,len(names)):
            names[i] = str(i+1) + ' '+names[i]
    with open('add_test.txt','w') as f1:
        f1.writelines(names)

#反爬，爬虫机制robots.txt,二进制的可以用re.content解码
def pa1():
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.83 Safari/535.11"}
    re = requests.get('https://www.zhihu.com', headers = headers)
    print(re.status_code)
def pa2():
    soup = BeautifulSoup(re.text,'lxml')
    print(soup.text)









