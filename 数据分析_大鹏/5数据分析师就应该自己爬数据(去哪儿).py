# -*- coding: utf-8 -*-
# @File    : 4数据分析师就应该自己爬数据.py
# @Date    : 2019-05-17
# @Author  : Zhang.Cookie

import requestes
from bs4 import BeautifulSoup
import pandas as pd

#获取多个网页
def qunaer():
    url_lst = []
    #url = "https://travel.qunar.com/search/place/22-shanghai-299878/0-----0/"
    url = "https://travel.qunar.com/p-cs299878-shanghai-jingdian-1-"
    for i in range(1,10):
        url_lst.append(url+str(i))
    # print(url_lst[0])

    r = requests.get(url_lst[0])
    soup = BeautifulSoup(r.text,'lxml')
    # print(soup)
    playname = []

    ul = soup.find('ul',class_ = "list_item clrfix")
    li = ul.find_all('li')
    for i in range(1,10):
        li1 = li[i]
        dic = {}
        dic["景点名称"] = li1.find('span',class_ = "cn_tit").text
        dic["景点攻聂"] = li1.find('div',class_ = "strategy_sum").text
        dic["点评数量"] = li1.find('div',class_ = "comment_sum").text
        dic["星级"] = li1.find('span',class_ = "total_star").find('span')['style'].split(':')[1]  #查找属性
        dic["排名"] = li1.find('span',class_ = "ranking_sum").text
        playname.append(dic)
    print(playname)
# qunaer()

def big():
    urllst = []
    ui = 'https://travel.qunar.com/p-cs299878-shanghai-jingdian-1-'
    for i in range(1,4):
        urllst.append(ui +str(i))  #得到多个网址
    datai = []
    n=0
    for ui in urllst:
        r = requests.get(ui)
        soup = BeautifulSoup(r.text, 'lxml')
            # 访问数据
        ul = soup.find('ul',class_="list_item clrfix")  #选取与数据最近的div
        li = ul.find_all('li')
            # 解析标签
        for i in li:
            n+=1
            dic = {}
            dic['lat'] = i['data-lat']
            dic['lng'] = i['data-lng']
            dic['景点名称'] = i.find('span',class_="cn_tit").text
            dic['攻略提到数量'] = i.find('div',class_="strategy_sum").text
            dic['点评数量'] = i.find('div',class_="comment_sum").text
            dic['景点排名'] = i.find('span',class_="ranking_sum").text
            dic['星级'] = i.find('span',class_="total_star").find('span')['style'].split(':')[1]
            datai.append(dic)
            print('成功采集%i条数据' % n)
    df = pd.DataFrame(datai)
    print(df)
big()

# for i in range(5):  #外层循环控制圈数
#     print("第%s圈"% i)
#     for j in  "123":
#         print("二循环第%s圈" % j)















