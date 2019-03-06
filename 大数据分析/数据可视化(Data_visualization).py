# -*- coding: utf-8 -*-
# @File    : 数据可视化(Data_visualization).py
# @Date    : 2019-02-21
# @Author  : Zhang.Cookie

import numpy as np
import matplotlib.pyplot as mp

#数据可视化
"""
x = np.linspace(-np.pi,np.pi,2000)
cos_y = np.cos(x) / 2
sin_y = np.sin(x)
mp.figure('Cookie image',figsize = (12,8),dpi=60,facecolor='lightgray')
#mp.figure(图形对象名，figsize = 窗口大小，dpi=分辨率，facecolor=颜色)
mp.title('Cookie image')
xo = np.pi * 3 / 4
yo_cos = np.cos(xo) / 2  #np 可对矢量和标量操作
yo_sin = np.sin(xo)
# mp.xlim(x.min(),x.max())
# mp.ylim(sin_y.min(),sin_y.max()) #去掉空白
#mp.yticks([-1,-0.75],['a','b'])   #刻度位置数组，刻度文本数组
#mp.xticks([-3,-2,-1],['π'])
#mp.xticks([-3,-2,-1],[r'$-\pi$',r'$-\frac{\pi}{2}$'])        #加上r是去掉python转义,加$$代表要做格式化转义，-π,2/π
ax = mp.gca()  #处理轴的函数
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
#ax.spines['right'].set_color(("red"))    #指定轴颜色
ax.spines['right'].set_color(("none"))
ax.spines['top'].set_color(("none"))
mp.plot(x,cos_y, linestyle = '--',linewidth = 6 ,color = 'dodgerblue',label =r'$y=\frac{1}{2}coas(x)$' )
#(水平坐标数组,垂直坐标数组,线型,线宽,线色,图例文本) 画图函数
mp.plot(x,sin_y,label = r'$y=sin(x)$')
mp.plot([xo,xo],[yo_cos,yo_sin],linestyle='--',linewidth=1 ,color = 'dodgerblue') #二点间画线
mp.legend(loc = 'upper left') #显示图例在那个位置
mp.scatter([xo,xo],[yo_cos,yo_sin],s =120,edgecolor="limegreen",facecolor = "white",zorder = 4)
#(水平坐标数组,垂直坐标数组,点型,大小,勾边色,填充色，z序(0,1)) 画点函数
mp.annotate(r'$\frac{1}{2}cos(\frac{3\pi}{4})=-\frac{\sqrt{2}}{4}$',#\frac是分数,\sqrt根号
            xy=(xo,yo_cos),xycoords='data',#data 数据坐标系
            xytext = (-90,-40),textcoords = 'offset points', #向下偏移，pffset points水平坐标系
            fontsize = 14,
            arrowprops = dict(arrowstyle = '- >',connectionstyle='arc3,rad=.2')) #arc3圆弧，rad半径
#(备注文本,xy=目标位置，xycoords=目标坐标系，xytest=文本位置，textcoords=文本坐标系，fontsize=字体大小,arrowprops=箭头属性)
mp.annotate(r'$sin(\frac{3\pi}{4})=\frac{\sqrt{2}}{2}$',#\frac是分数,\sqrt根号
            xy=(xo,yo_sin),xycoords='data',#data 数据坐标系
            xytext = (20,20),textcoords = 'offset points',
            fontsize = 14,
            arrowprops = dict(arrowstyle = '- >',connectionstyle='arc3,rad=.2')) #arc3圆弧，rad半径
mp.show()

#轴 spines
#图例 label
#二点连线|画线,plot
#备注 annotate
#图形对象 figure
"""

#子图
#缺省布局
# mp.subplot(行数，列数，图号)
#栅格布局
#import matplotlib.gridspec as mg
#gs = mg.GridSpec(行数，列数) #栅格布局
#mp.subplot(gs[行列])
#自由布局
#mp.axes([左下角水平坐标，右下角垂直坐标，宽度，高度])  所有尺寸参数都是相对比例

#坐标刻度定位器，类似直尺上的标量
#定位器对象 = mp.xxxLocator(..)
#ax  = mp.gca()
#ax.xaxis.ser_major_locator(定位器对象) #主刻度
#ax.xaxis.ser_major_locator(定位器对象) #次刻度


#散点图
"""
n = 1000
x = np.random.normal(0,1,n)   #平均值(value=0)，标准差()，个数  ；标准分布
y = np.random.normal(0,1,n)
d = np.sqrt(x ** 2 + y ** 2) #距离。。
mp.figure('Scatter',facecolor='lightgray')
mp.title('Scatter',fontsize = 20)
mp.xlabel('x',fontsize = 14) #水平坐标
mp.ylabel('y',fontsize = 14 )# 垂直坐标
mp.tick_params(labelsize = 10)
mp.grid(linestyle = ':')
mp.scatter(x,y,s=60,c=d ,cmap='jet_r',alpha= 0.5,marker ='o')
#scatter画散点图  c=d 颜色=距离要与cmap(颜色映射)同用,正向映射(jet)反向(jet_r),alpha透明度,marker图形（*，d..）
mp.show()
"""

#区域填充
#mp.fill_between(水平坐标数组，垂直坐标起点数组，垂直坐标终点数组,条件，color=颜色，alpha=透明度)
#柱状图
#mp.bar( 水平坐标数组，高度数组，ec=边缘色，fc= 填充se，label=标签文本)
#等高线图
#mp.contour(x,y,z,线数，colors,linewidths)
#mp.contourf(x,y,z,线数，cmap=颜色映射)
#热像图
#mp.imshow(矩阵，cmap=颜色映射，origin=垂直轴方向)







































