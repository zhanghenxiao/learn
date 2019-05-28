# -*- coding: utf-8 -*-
# @File    : 1十大易错点.py
# @Date    : 2019-05-15
# @Author  : Zhang.Cookie

import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get(url = 'https://book.douban.com/latest')
print(r.encoding, r.status_code, r.encoding) #200 访问成功的显示
print(r.url)
# print(r.text)

soup = BeautifulSoup(r.text,'lxml') # pip install lxml   数据解析
# print(soup)
# print(soup.title,soup.a)  #提取标签（标题，第一个a 标签）
# print(soup.a.name,soup.a.attrs,soup.a.text) #可操作对象（标签，属性，元素）
# print(soup.title.text)  #提取标签文本
## 如何查找标签？ → find() /find_all()
# find() → 查找单个标签 (可访问元素，属性)
# url = soup.find('div',class_= "grid-12-12 clearfix").find('a',class_ = "cover").attrs['href']  #有趣表达式https://book.douban.com/subject/33404843/
# print(url)
## find_all() → 查找所有标签
urls = soup.find('div',class_= "grid-12-12 clearfix").find_all('a')
# print(urls[::2])
#print(urls[::2])  #步距为2
url_lst = []
for url in urls[::2]:
    url_lst.append(url['href'])  #保存所有url
# print(url_lst)
#数据采集
def get():
    urls = requests.get("https://book.douban.com/latest")
    soup = BeautifulSoup(urls.text,'lxml')
    soups = soup.find_all('div',class_="detail-frame")
    #print(soups)
    lst = []
    for i in soups:
        dic = {} #输出清晰
        dic['书名'] = i.find('h2').text.replace('\n','')
        dic['评分'] = i.find_all('p')[0].text.replace('\n', '').replace('', '')
        dic['作者'] = i.find_all('p')[1].text.replace('\n', '').replace('', '')
        dic['简介'] = i.find_all('p')[2].text.replace('\n', '').replace('', '')
        lst.append(dic)
    return lst
result =get()

df = pd.DataFrame(result)
print(df)




