# 来自官方文档 https://pillow.readthedocs.io/en/stable/reference/Image.html

#第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果 --------
#-------- ImageDraw Moudle --------
图片上画线条
import sys
from PIL import Image,ImageDraw

im = Image.open("th.png")
draw = ImageDraw.Draw(im) #实例化一个对象
draw.line((0, 0) + im.size, fill=128, width=5)
draw.line((0, im.size[1], im.size[0], 0), fill=128)
draw.line((0,im.size[1]/2)+(im.size[0]/2,im.size[1]), fill=128, width=5)
im.show()
图片上写字
from PIL import Image, ImageDraw, ImageFont
# get an image
base = Image.open('th.jpg').convert('RGBA')
# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))
# get a font  需要在C:\Windows\Fonts拷贝一份字体文件 当前脚本路径下
fnt = ImageFont.truetype('cambriai.ttf', 40)
# get a drawing context
d = ImageDraw.Draw(txt)
# draw text, half opacity
d.text((10,10), "Hello", font=fnt, fill=(255,255,255,128))
# draw text, full opacity
d.text((10,60), "World", font=fnt, fill=(255,255,255,255))
fillcolor = "#ff0000"   #字体颜色
d.text((base.size[0]-20,10), "4", font=fnt, fill=fillcolor)
out = Image.alpha_composite(base, txt)
out.show()

#第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
#第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
# import random
# def creat_num(num,long):
#     str = 'qwertyuiopasdfghjklzxcvbnm1234567890'
#     b = []
#     for i in range(num):
#         a = ''
#         for j in range(long):
#             a += random.choice(str)
#         b.append(a)
#     print(b)
# creat_num(200,10)

#第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。
#参考文档：https://docs.python.org/2/library/collections.html#module-collections
#https://www.jb51.net/article/48771.htm
# 1.namedtuple(): 生成可以使用名字来访问元素内容的tuple子类
# 2.deque: 双端队列，可以快速的从另外一侧追加和推出对象
# 3.Counter: 计数器，主要用来计数
# 4.OrderedDict: 有序字典
# 5.defaultdict: 带有默认值的字典
# import os
# from collections import Counter
#
# with open("4.txt",'r') as fp:
#     #txt = fp.read().split(' ')   #分割成单词
#     txt = fp.read()
#     c = Counter(txt)   #输出字母出现的次数
#     print(c)
#     print(c.most_common(5)) #出现次数最多的五个字母








