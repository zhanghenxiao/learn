# coding: utf-8

import math
import random
import pygame
import sys
from pygame.locals import *

#参考链接 20个游戏项目 https://github.com/CharlesPikachu/Games
# 画线
def draw():
    # 初始化pygame
    pygame.init()
    # 设置窗口的大小，单位为像素
    screen = pygame.display.set_mode((500, 400))
    # 设置窗口标题
    pygame.display.set_caption('Hello World')
    #定义颜色
    BLUE = (0,0,255)
    pygame.draw.line(screen,BLUE,[0,0],[50,30],5)
    # 程序主循环
    while True:
        # 获取事件
        for event in pygame.event.get():
            # 判断事件是否为退出事件
            if event.type == QUIT:
                # 退出pygame
                pygame.quit()
                # 退出系统
                sys.exit()

        # 绘制屏幕内容
        pygame.display.update()
#draw()

#实现动画效果
def donghua():
    # 初始化pygame
    pygame.init()
    # 设置帧率（屏幕每秒刷新的次数）
    FPS = 3000
    # 获得pygame的时钟
    fpsClock = pygame.time.Clock()
    # 设置窗口大小
    screen = pygame.display.set_mode((500, 400), 0, 32)
    # 设置标题
    pygame.display.set_caption('Animation')
    # 定义颜色
    WHITE = (255, 255, 255)
    # 加载一张图片（所用到的的图片请参考1.5代码获取）
    test = r"C:\Users\succful\Desktop\opencvStudy\pic\firefox.png"
    img = pygame.image.load(test)
    # 初始化图片的位置
    imgx = 10
    imgy = 10
    # 初始化图片的移动方向
    direction = 'right'
    # 程序主循环
    while True:
        # 每次都要重新绘制背景白色
        screen.fill(WHITE)
        # 判断移动的方向，并对相应的坐标做加减
        if direction == 'right':
            imgx += 5
            if imgx == 380:
                direction = 'down'
        elif direction == 'down':
            imgy += 5
            if imgy == 300:
                direction = 'left'
        elif direction == 'left':
            imgx -= 5
            if imgx == 10:
                direction = 'up'
        elif direction == 'up':
            imgy -= 5
            if imgy == 10:
                direction = 'right'
        # 该方法将用于图片绘制到相应的坐标中
        screen.blit(img, (imgx, imgy))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # 刷新屏幕
        pygame.display.update()
        # 设置pygame时钟的间隔时间
        fpsClock.tick(FPS)
donghua()

def donghua2():
    # 初始化pygame
    pygame.init()
    # 设置帧率（屏幕每秒刷新的次数）
    FPS = 30
    # 获得pygame的时钟
    fpsClock = pygame.time.Clock()
    # 设置窗口大小
    screen = pygame.display.set_mode((500, 400), 0, 32)
    # 设置标题
    pygame.display.set_caption('Animation')
    # 定义颜色
    WHITE = (255, 255, 255)
    # 加载一张图片（所用到的的图片请参考1.5代码获取）
    zhu = r"game_pic\zhu1.png"
    zhu_img = pygame.image.load(zhu)
    bad = r"game_pic\badguy.png"
    bad_img = pygame.image.load(bad)
    mao = r'game_pic\mao.png'
    mao_img = pygame.image.load(mao)
    # 初始化图片的位置
    imgzhux = 10
    imgzhuy = 10
    height = (500 - 2) / 4
    for i in range (3):
        imgbadx = height+ (height * i)
        imgmaox = height+ (height * i)
    imgbady = 30
    imgmaoy = 200
    # 初始化图片的移动方向
    direction = 'down'
    # 程序主循环
    while True:
        # 每次都要重新绘制背景白色
        screen.fill(WHITE)
        # 判断移动的方向，并对相应的坐标做加减
        if direction == 'down':
            imgbady += 5
            if imgbady == 400:
                direction = 'right'
        # # 该方法将用于图片绘制到相应的坐标中

        for i in range(3):
            screen.blit(zhu_img, (height+ (height * i), imgzhuy))
        screen.blit(bad_img, (imgbadx,imgbady))
        # screen.blit(mao_img, (imgmaox, imgmaoy))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # 刷新屏幕
        pygame.display.update()
        # 设置pygame时钟的间隔时间
        fpsClock.tick(FPS)
#donghua2()
