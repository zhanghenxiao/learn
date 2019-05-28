# -*- coding: utf-8 -*-
# @File    : 语音.py
# @Date    : 2019-05-24
# @Author  : Zhang.Cookie

from win32com.client import constants
import aiml
#import speech
import os
import win32com.client
import pythoncom
import itchat,requests
from itchat.content import *

# speaker = win32com.client.Dispatch("SAPI.SPVOICE")
# speaker.Speak("测试完成")

# os.chdir('./alice') # 将工作区目录切换到刚才复制的alice文件夹
# alice = aiml.Kernel()
# alice.learn("startup.xml")
# alice.respond('LOAD ALICE')
# alice.respond('hello')

import speech,os
#AI
def Ai():
    while True:
        say = speech.input()  # 接收语音
        speech.say("you said:" + say)  # 说话
        if say == "你好":
            speech.say("How are you?")
        elif say == "天气":
            speech.say("今天天气晴!")
        elif say == "打开记事本":
            os.system("notepad.exe")
Ai()
#API 接口测试
def API():
    while True:
        key = "5a6deea7a2914048852798a0421ea0ee"  #机器人ID
        uid = "vaster"
        #msg = "返回一个网址链接"
        msg  = speech.input()
        api_tuling = "http://www.tuling123.com/openapi/api"
        data = {
            'key' : key,
            'info':msg,
            'userid':uid,
        }
        ret = requests.post(api_tuling,data=data).json()
        speech.say(ret.get('text'))
        print(ret)
# 初步实现
def test():
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

# import speech
# import time
# response = speech.input("Say something, please.")
# speech.say("You said " + response)
# def callback(phrase, listener):
#     if phrase == "goodbye":
#         listener.stoplistening()
#         speech.say(phrase)
#         print(phrase)
# listener = speech.listenforanything(callback)
# while listener.islistening():
#     time.sleep(.5)
















