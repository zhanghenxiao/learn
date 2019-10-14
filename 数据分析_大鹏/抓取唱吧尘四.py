# -*- coding: utf-8 -*-
# @File    : 抓取唱吧尘四.py
# @Date    : 2019-09-12
# @Author  : Zhang.Cookie

# src="http://qiniuuwmp3.changba.com/1129259339.mp4"></video>
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as mp
from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType
import os
import re


def get(url):
    try:
        # 爬取歌曲主页面
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'lxml')
        # print(type(soup))
        # print(soup)
        tags = soup.find('div', class_="userPage-tab-content userPage-tab-active-content").find_all('li')
        hrefs = re.findall(r'a href=(.*)style', str(tags))  # 匹配=之后，style之前的字符串 ，精辟！！！！
        return hrefs
    except:
        raise


def get_mp3():
    url = "http://changba.com/u/349478224"  # 唱吧主页
    s = get(url)
    # print(s)
    mp3_url_list = []
    mp3_url_name = []
    mp4_url_list = []
    for i in s:
        w = re.search(r"/(.*)", str(i)).group()
        name_url = "http://changba.com" + w

        html = requests.get(name_url)
        soup = BeautifulSoup(html.text, 'lxml')
        # print(soup)
        s = re.findall(r'var a=(.*),b=', str(soup))  # mp3 url
        mp3_url = (removePunctuation(s))
        if (mp3_url) == "":
            s = re.findall(r'data-workid=(.*)', str(soup))  # mp4 url
            # print(s)
            mp4_url = (removePunctuation(s[0]))
            oneurl = "http://qiniuuwmp3.changba.com/"
            mp4_url = oneurl+mp4_url+".mp4"
            mp4_url_list.append(mp4_url)
        else:
            # mp3_url_list.append(mp3_url)
                html = requests.get(name_url)
                # print(name_url)
                soup = BeautifulSoup(html.text, 'lxml')
                tags = soup.find('div', class_="widget-player")
                mp3_name = tags.find('div', class_="title")
                mp3_name = mp3_name.text
                mp3_url_list.append(mp3_url)
                mp3_url_name.append(mp3_name)
                # return mp3_url,mp3_name
    return  mp3_url_list,mp3_url_name


def download_mp3():
    mp3_url_list, mp3_url_name = get_mp3()
    for url in mp3_url_list:
        for name in mp3_url_name:
            root = "E://quanminsongs//"
            # path = root + "//" + song_name + "-" + geming + ".m4a"
            path = root + name + ".mp3"
            try:
                if not os.path.exists(root):
                    os.mkdir(root)
                print("正在下载" + "  " + name)
                if not os.path.exists(path):
                    rqt = requests.get(url)
                    with open(path, 'wb') as f:
                        f.write(rqt.content)
                        f.close()
                        print("下载成功")
                else:
                    print("文件已存在，下载失败")
            except:
                raise
#链接有问题。。
def download_mp4():
    url = "http://qiniuuwmp3.changba.com/1121699044.mp4"
    root = "E://quanminsongs//"
    # path = root + "//" + song_name + "-" + geming + ".m4a"
    name = 'tttt'
    path = root + name + ".mp4"
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        print("正在下载" + "  " + name)
        if not os.path.exists(path):
            rqt = requests.get(url)
            with open(path, 'wb') as f:
                f.write(rqt.content)
                f.close()
                print("下载成功")
        else:
            print("文件已存在，下载失败")
    except:
        raise

# 去除str 中符号
def removePunctuation(text):
    punctuation = '>[{？!,;+"\''
    text = re.sub(r'[{}]+'.format(punctuation), '', str(text))
    punctuation = ']'
    text = re.sub(r'[{}]+'.format(punctuation), '', str(text))
    return text.strip().lower()


if __name__ == '__main__':
    # url = "http://changba.com/u/349478224"  #唱吧主页
    #get(url)
    # get_mp3()

    # data-workid = "1099563963"
    # nameurl = "http://qiniuuwmp3.changba.com/1129259339.mp4"
    download_mp3()
    # download_mp4()
