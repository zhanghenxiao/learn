# -*- coding: utf-8 -*-
# @File    : 10豆瓣影评分析.py
# @Date    : 2019-05-29
# @Author  : Zhang.Cookie

import  requests
from bs4 import BeautifulSoup
import pandas as pd

# u1 = "https://movie.douban.com/subject/26100958/comments?start=0&limit=20&sort=new_score&status=P"
def urls():  #获取多个网址
    urllist = []
    value = [x * 10 for x in range(1, 40) if x % 2 == 0]  #列表生成式
    for i in value:
       urllist.append("https://movie.douban.com/subject/26100958/comments?start=%d&limit=20&sort=new_score&status=P"%i )
    return urllist
urllist = urls()
def data():
    spanlist = []  #放在循环之外
    for i in urllist:
        re = requests.get(i)
        soup = BeautifulSoup(re.text,'lxml')
        span = soup.find_all('span',class_='short')
        for i in span:
            spanlist.append(i.text)
    df = pd.DataFrame({'影评':spanlist})
    return df
df = data()
txt = str(df.values)
dic = {}
name = ['黑寡妇','灭霸','美队','钢铁侠','雷神','奇异博士','星爵','浩克','黑豹','蜘蛛侠','惊奇队长']
for i in name:
    dic[i] = txt.count(i)
print(dic)  #{'黑寡妇': 7, '灭霸': 19, '美队': 15,}
df = pd.DataFrame(dic.values(),dic.keys())
#df.to_excel('./10.xls')  #导出到excel中










