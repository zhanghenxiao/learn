# -*- coding: utf-8 -*-
# @File    : 抓取飞全民K歌.py
# @Date    : 2019-09-05
# @Author  : Zhang.Cookie

import  requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as mp
from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType
import os
import re

#中文提取参考链接 https://blog.csdn.net/a786150017/article/details/86004004
#BeautifulSoup 模块使用指南  https://www.jianshu.com/p/2b783f7914c6
#k 歌  https://github.com/Mrliu8023/getquanmin
def get_url():
        url = "https://kg.qq.com/node/personal?uid=6b9e9c82212a338a&tdsourcetag=s_pcqq_aiomsg"
        re = requests.get(url)
        soup = BeautifulSoup(re.text,'lxml')
        soups = soup.find_all('div', class_="mod_playlist__box")
        # print(soups)
        allge = []
        n = 0
        for i in soups:
                n+=1
                dic = {}
                dic['test'] = i.find('script', type="text/javascript").text
                # dic['歌名'] = i.find('a', class_="mod_playlist__work").text.replace('主打', '')
                # dic['留言次数'] = i.find_all('span', class_="mod_playlist__record")[0].text #
                # dic['播放次数'] = i.find_all('span', class_="mod_playlist__record")[1].text
                # dic['歌曲链接'] = i.find_all('a',href='').text
                allge.append(dic)
                # print('成功采集%i条数据' % n)
        df = pd.DataFrame(allge)
        print(df)
        # return df
def getHtmlMessage(url):
    try:
        # 爬取歌曲主页面
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'lxml')
        # print(type(soup))
        # print(soup)
        # 正则提取歌曲信息
        data = re.findall(r'window.__DATA__ =(.*)',soup.text)
        c = (re.findall(r'"singer_name":(.*)',str(data)))    #获取歌曲作者
        testname = re.split(',',str(c))[0]
        name = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fa5]", '', testname)

        d = (re.findall(r'"song_name":(.*)', str(data)))    #获取歌名
        testgeming = re.split(',', str(d))[0]
        geming = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fa5]", '', testgeming)

        u = (re.findall(r'"playurl":(.*)', str(data)))  #获取歌曲链接
        testurl = re.split(',', str(u))[0]
        nameurl = (removePunctuation(testurl))

        return name,geming,nameurl

    except:
       print("爬取网页失败")
def a_herflist():
    url = "https://kg.qq.com/node/personal?uid=6b9e9c82212a338a&tdsourcetag=s_pcqq_aiomsg"  # 主页
    try:
        # 爬取歌曲主页面
        html = requests.get(url)
        print(html.encoding)
        soup = BeautifulSoup(html.text, 'lxml')
        tags = soup.find_all('li', class_="mod_playlist__item")
        a_herflist = []
        for tag in tags:
            a_herf = tag.a["href"]   #获取播放歌曲跳转链接
            # a_img_alt = tag.a.img['alt']  #
            # a_class = tag.p.a['class']
            # print(tag.p)
            # span_class = tag.p.span['class']  #
            print(a_herf)
            a_herflist.append(a_herf)
        return a_herflist

    except:
        print("爬取网页失败")
def getmp3(url):
    """
    下载mp3
    """
    message = getHtmlMessage(url)
    # 获取歌手名
    singer = message.group(1)
    # 获取歌名
    song_name = message.group(3)
    # 获取歌曲链接
    songurl = message.group(2)
    # 设置下载路径(以歌手名做文件夹名称)  linux下请自行设置
    root = "E://quanminsongs//" + singer
    path = root + "//" + song_name + "-" + singer + ".m4a"
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        print("正在下载" + "      " + song_name)
        if not os.path.exists(path):
            rqt = requests.get(songurl)
            with open(path, 'wb') as f:
                f.write(rqt.content)
                f.close()
                print("下载成功")
        else:
            print("文件已存在，下载失败")
    except Exception as c:
        print("爬取失败")
def download():
    hreflist = a_herflist()
    for url in list(hreflist):
    # url = "https://node.kg.qq.com/play?s=PfReO8Pi6kJq3PyR&g_f=personal"
        song_name,geming,nameurl = getHtmlMessage(url)
        root = "E://quanminsongs//"
        path = root + "//" + song_name + "-" + geming + ".m4a"
        try:
            if not os.path.exists(root):
                os.mkdir(root)
            print("正在下载" + "   " + geming)
            if not os.path.exists(path):
                rqt = requests.get(nameurl)
                with open(path, 'wb') as f:
                    f.write(rqt.content)
                    f.close()
                    print("下载成功")
            else:
                print("文件已存在，下载失败")
        except Exception as c:
            print("爬取失败")
# 去除str 中符号
def removePunctuation(text):
    punctuation = '[{？!,;+"\''
    text = re.sub(r'[{}]+'.format(punctuation), '', text)
    return text.strip().lower()

if __name__ == '__main__':
    # url = "https://kg.qq.com/node/personal?uid=6b9e9c82212a338a&tdsourcetag=s_pcqq_aiomsg"  #主页
    # url = "https://node.kg.qq.com/play?s=PfReO8Pi6kJq3PyR&g_f=personal"  #理想歌曲页
    # getHtmlMessage(url)

    #songurl = "http://cgi.kg.qq.com/fcgi-bin/fcg_get_play_url?shareid=tzXMj-tqV2giltuX"
    # songurl = "http://tx.stream.kg.qq.com/shkge-btfs/e2a4b59e168cfd3e8bae770b2600ded134a64950?"

    download()



















