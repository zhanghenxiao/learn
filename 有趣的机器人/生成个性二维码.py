# -*- coding: utf-8 -*-
# @File    : 生成个性二维码.py
# @Date    : 2019-03-08
# @Author  : Zhang.Cookie

import qrcode
from  PIL import Image
from MyQR import myqr
import os

#简易二维码
qr_image = qrcode.make("迢迢牵牛星,皎皎河汉女."
                       "纤纤擢素手,札札弄机杼."
                       "终日不成章,泣涕零如雨."
                       "河汉清且浅,相去复几许."
                       "盈盈一水间,脉脉不得语."
                       "--- ,Cookie设计的个性二维码")
qr_image.save("baidu.png")
#print(qrcode.__file__) #引用路劲


#微调二维码
"""
qr = qrcode.QRCode(
    version = 2 , #version:版本 v1-40 （v-1）*4+21 格子数量
    error_correction = qrcode.constants.ERROR_CORRECT_Q , #容错系数L7 M15 Q25 h30
    box_size = 8,  #像素点
    border=4     #空白大小
)
qr.add_data("http://www.51bbw.cn/")
qr.make(fit=True)  #编译数据
img = qr.make_image(back_color="red")
img.save("redbaidu.png")
"""

#添加logo二维码
"""
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_H, # 用于控制二维码的错误纠正程度, 设置容错率为最高
    box_size=8, # 控制二维码中每个格子的像素数，默认为10
    border=1, # 二维码四周留白，包含的格子数，默认为4
    #image_factory=None,  保存在模块根目录的image文件夹下
    #mask_pattern=None
   )
url1 = "迢迢牵牛星,皎皎河汉女.纤纤擢素手,札札弄机杼.终日不成章,泣涕零如雨.河汉清且浅,相去复几许.盈盈一水间,脉脉不得语.--- ,Cookie设计的个性二维码"
url = "http://www.51bbw.cn/"
qr.add_data(url1) # QRCode.add_data(data)函数添加数据
qr.make(fit=True)  # QRCode.make(fit=True)函数生成图片

img = qr.make_image(fill_color="white",back_color="orange")  #填充色，
img = img.convert("RGBA") # 二维码设为RGB格式 彩色
logo = Image.open('x.jpg') # 传gif生成的二维码会没有动态效果，对应系统文件夹可查看动态效果
w , h = img.size
logo_w , logo_h = logo.size
factor = 2.5   # 默认logo最大设为图片的四分之一
s_w = int(w / factor)
s_h = int(h / factor)
if logo_w > s_w or logo_h > s_h:
    logo_w = s_w
    logo_h = s_h
logo = logo.resize((logo_w, logo_h), Image.ANTIALIAS)
l_w = int((w - logo_w) / 2)
l_h = int((h - logo_h) / 2)
logo = logo.convert("RGBA")
img.paste(logo, (l_w, l_h), logo)
#img.show()
img.save("x.png")
"""

#动图二维码
"""
words = "http://www.51bbw.cn/"
picture = "x.jpg"
output_name = "x.png"
try:
    version,level,qr_name = myqr.run(
        words,
        version = 1,
        level='H',    #容错度
        picture = picture,
        colorized= True,
        contrast=2.0,   #  对比度
        brightness=1.0, # 亮度
        save_name=output_name,
        save_dir=os.getcwd()  #当前路劲
    )
except:
    raise
"""




