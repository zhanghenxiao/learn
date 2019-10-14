# -*- coding: utf-8 -*-
# @File    : 13下载图片.py
# @Date    : 2019-05-29
# @Author  : Zhang.Cookie

import requests
from bs4 import BeautifulSoup
import os

url = "https://movie.douban.com/subject/26584183/photos?type=S&start=60&sortby=like&size=a&subtype=a"
re = requests.get(url)
print(re)
soup = BeautifulSoup(re.text,'lxml')   #H获取信息有问题，但是逻辑完美
div = soup.find('div',class_="article")
ul = soup.find('ul')
li = soup.find_all('li')
lis = li[60]
img = lis.find('img')
print(img)
imgs = []
for i in lis:
    im = i.find('img')
    imgs.append(im['src'])
photo = imgs[0]
os.chdir('C:\\Users\\succful\\Desktop\\13\\')
imgr = requests.get(url=photo)
with open('p1.jpg','wb') as f:
    f.write(imgr.content)




