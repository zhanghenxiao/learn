# -*- coding: utf-8 -*-
# @File    : 6找到一个城市有趣的地方.py
# @Date    : 2019-05-28
# @Author  : Zhang.Cookie

import requestes
from bs4 import BeautifulSoup
url = "https://travel.qunar.com/p-cs299878-shanghai-jingdian-1-"

ur = requestes.get(url)
soup = BeautifulSoup(ur.text,'lxml')
tex = soup.find_all('span',class_='cn_tit')  #获取该页面的所有景区，特别注意text别乱加
print(type(tex))  #<class 'bs4.element.ResultSet'>
for i in tex:
    print(type(i),i.text) #<class 'bs4.element.Tag'>


# 创建函数，获取数据
def get_urls(ui,n):
    # ui：基础页面
    # n：获取页码数
    urllsti = []
    for i in range(1,n+1):
        urllsti.append(ui +str(i))
    return urllsti

get_urls('https://travel.qunar.com/p-cs299914-beijing-jingdian-1-',5)

def get_data(u):
    # u：输入网址
    ri = requests.get(u)
    # requests访问网站
    soupi = BeautifulSoup(ri.text, 'lxml')
    # bs解析页面
    infori = soupi.find('ul', class_="list_item clrfix").find_all('li')
    # 获取列表内容

    datai = []
    n = 0
    for i in infori:
        n += 1
        # print(i.text)
        dic = {}
        dic['lat'] = i['data-lat']
        dic['lng'] = i['data-lng']
        dic['景点名称'] = i.find('span', class_="cn_tit").text
        dic['攻略提到数量'] = i.find('div', class_="strategy_sum").text
        dic['点评数量'] = i.find('div', class_="comment_sum").text
        dic['景点排名'] = i.find('span', class_="ranking_sum").text
        dic['星级'] = i.find('span', class_="total_star").find('span')['style'].split(':')[1]
        datai.append(dic)
        # 分别获取字段内容
    return datai


print(get_data(get_urls(1,1)[:2]))# 测试：显示第一页的前2条数据
