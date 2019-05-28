# -*- coding: utf-8 -*-
# @File    : 微信聊天机器人.py
# @Date    : 2019-03-06
# @Author  : Zhang.Cookie

import itchat,requests
from itchat.content import *

#登陆，，发送消息
"""
itchat.auto_login(hotReload=True) #登陆
itchat.send("hello world",toUserName="filehelper") #给文件助手发送消息
#print(itchat.get_friends()) #获取所有好友
nickname = itchat.get_friends()[1]['NickName'] #获取最近一次好友名
username = itchat.get_friends()[1]['UserName']  #微信随机生成的字符串每次不唯一
#print(nickname,username)
nickname1 = itchat.get_friends()[0]['NickName']  #获取的本机用户
username1 = itchat.get_friends()[0]['UserName']
print(nickname1,username1)
itchat.send("hello world",toUserName= nickname1)
itchat.send("hello world",toUserName= username1)     #发送消息给朋友（有问题）
# # uname = itchat.search_friends(name = "郑健强")     #查找微信好友
# print(uname)
# itchat.send("hello world",toUserName= '零度温柔' )
"""
#简版的聊天机器人
"""
@itchat.msg_register('Text')  #装饰器监听文本
def text_reply(msg):
    if msg['Text'] == "你好":
        return "很高兴认识你"
    else:
        return "[代码微信机器人自动回复]注意你和大佬的说话态度"
@itchat.msg_register('File')
def file_reply(msg):
    return "[代码微信机器人自动回复]不要发图"
@itchat.msg_register('Image')
def file_reply(msg):
    return "[代码微信机器人自动回复]注意你的态度"
itchat.auto_login(hotReload=True)
itchat.run()  #监听
"""
#接口测试：调用图灵机器人
key = "5a6deea7a2914048852798a0421ea0ee"  #机器人ID
uid = "vaster"
msg = "返回一个网址链接"
api_tuling = "http://www.tuling123.com/openapi/api"
data = {
    'key' : key,
    'info':msg,
    'userid':uid,
}

ret = requests.post(api_tuling,data=data).json()
print(ret.get('MAP'))

#微信聊天机器人
def good():
    key = "5a6deea7a2914048852798a0421ea0ee"  #机器人ID(apikey)
    uid = "vaster"
    def get_reply(msg):
        api_tuling = "http://www.tuling123.com/openapi/api"  #图灵机器人接口
        data = {
            'key' : key,
            'info':msg,
            'userid':uid,
        }
        ret = requests.post(api_tuling,data=data).json()
        return ret.get('text')

    @itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING, PICTURE, RECORDING, VOICE, ATTACHMENT, VIDEO, FRIENDS, SYSTEM])
    def file_reply(msg):
        defaultmsg = msg['Text']
        reply = get_reply(defaultmsg)
        return reply
    @itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING, PICTURE, RECORDING, VOICE, ATTACHMENT, VIDEO, FRIENDS, SYSTEM]  #类型
                         ,isGroupChat=True)  # 所有群监听
    def group_replay(msg):
        if msg['isAt']:   #群里有人@ 才回答
            defaultmsg = msg['Text']
            return get_reply(defaultmsg)
        return  None
    itchat.auto_login(hotReload=True)  #登陆
    itchat.run()  # 监听












