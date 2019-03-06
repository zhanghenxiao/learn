# -*- coding: utf-8 -*-

# @File    : 连接mysql.py
# @Date    : 2019-01-11
# @Author  : Zhang.Cookie

import pymysql,xlrd,_thread,time
#mysql,连接数据库-----------
def conectmysql(threadname,t):
    # 打开数据库连接
    db = pymysql.connect("localhost","root","123","cookie" )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    print ("Database version : %s " % data) #数据库版本
    # 关闭数据库连接
    db.close()
#conectmysql()

#_thread ,threading 多线程--------------------

def thread1(threadName,delay):
    c = 0
    while c < 5:
        time.sleep(delay)
        c += 1
        print("%s:%s"%(threadName,time.ctime(time.time())))
def thread2(threadName,delay):
    c = 5
    while c > 0:
        time.sleep(delay)
        c =c - 1
        print("%s:%s"%(threadName,time.ctime(time.time())))
# try:
#     _thread.start_new_thread(thread1,("T1",2) )
#     _thread.start_new_thread(thread2,("T2",5) )
# except:
#     print("error:无法启动线程")
# while 1:
#     pass

#requests 抓取小说网页----------
#第一步获取整个网页
#第二步提取我们感兴趣的部分，xpath,beautiful soup
import requests
from bs4 import BeautifulSoup
def taobao():
    url = "https://login.taobao.com/member/login.jhtml?spm=a21bo.2018.201864-2.d1.5af911d9TwsuT4&f=top&redirectURL=http%3A%2F%2Fwww.taobao.com%2F"
    req = requests.get(url)
    print(req.text)
    with open("淘宝text", "w+", encoding='utf-8') as f:
        f.write(req.text)
        f.close()
#taobao()
def wandao():
    url2 = "https://www.ibiquge.net/13_13330/4327363.html"
    req = requests.get(url2)
    html = req.text
    bf = BeautifulSoup(html)
    # texts = bf.find_all('div',id="content")
    #print(texts[0].text.replace('\xa0' * 8, '\n\n')) #先去除br标签，在用teplace去除空格
    texts = bf.find_all('div',class_="box_con")
    print(texts) #先去除br标签，在用teplace去除空格
    # with open("一念成魔text", "w+", encoding='utf-8') as f:
    #     f.write(texts)
    #     f.close()
# wandao()
#requests 抓取图片========================
def testimage():
    src="fromurl=http://www.duitang.com/blog"
    req = requests.get(src)
    print(req.text)
testimage()
