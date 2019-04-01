# -*- coding: utf-8 -*-
# @File    : wx_1.py
# @Date    : 2019-03-11
# @Author  : Zhang.Cookie

import wx,os
#输出文本hello world
"""
app = wx.App()
window = wx.Frame(None, title="wxPython - www.yiibai.com", size=(400, 300))
panel = wx.Panel(window)
label = wx.StaticText(panel, label="Hello World", pos=(100, 100))
window.Show(True)
app.MainLoop()
"""

#位置为10的一个窗口
"""
app = wx.App()
window = wx.Frame(None, -1,"hello", pos = (10,10), size = (300,200),style = wx.CAPTION, name = "frame")
#None(parent窗口父类)，-1(id窗口标识)，Title,Pos(位置),size,style,name(对象内部名称)
window.Show(True)
app.MainLoop()
"""

#事件绑定
"""
def opefile(event): #事件函数有且只有一个参数，叫event
    path = path_text.GetValue()
    with open(path,"r",encoding="utf-8") as f:
        content_txt.SetValue(f.read())
app =wx.App()  #实例化一个主循环
frame = wx.Frame(None,title="cookie 记事本",pos=(500,500),size=(600,500)) #实例化一个窗口，
path_text = wx.TextCtrl(frame,pos = (5,5),size = (300,24),style=wx.TE_MULTILINE)  #文本框，位置，大小，wx.TE_MULTILINE支持多行
open_button = wx.Button(frame,label = "打开",pos = (350,5),size = (50,24))  #按钮，按钮文本
open_button.Bind(wx.EVT_BUTTON,opefile)  #绑定打开文件到open_button按钮上
save_button = wx.Button(frame,label = "保存",pos = (400,5),size = (50,24))
content_txt = wx.TextCtrl(frame,pos = (5,39),size = (475,300),style=wx.TE_MULTILINE) #一个文本框
frame.Show()  #调用窗口展示功能
app.MainLoop() #启动主循环
"""

#尺寸器,文本类，按钮,事件绑定
"""
def opefile(event):
    path = path_text.GetValue()
    with open(path,"r",encoding="utf-8") as f:
        content_text.SetValue(f.read())
app =wx.App()
frame = wx.Frame(None,title="cookie 记事本",pos=(500,500),size=(600,500))
panel = wx.Panel(frame)  #更好的控制布局和调整大小
path_text = wx.TextCtrl(panel)
open_button = wx.Button(panel,label = "打开")
open_button.Bind(wx.EVT_BUTTON,opefile)
save_button = wx.Button(panel,label="保存")
content_text= wx.TextCtrl(panel,style = wx.TE_MULTILINE) #不加wx.TE_MULTILINE则为一行，TextCtrl可编辑文本类

staic_text = wx.StaticText(panel)   #StaticText只读文本类
txt = "这是cookie的logo"
font=wx.Font(18,wx.DECORATIVE,wx.ITALIC,wx.NORMAL)  #指定字体的静态文本的font
staic_text.SetFont(font)
staic_text.SetLabel(txt)

box = wx.BoxSizer() #不带参数表示默认实例化一个水平尺寸器
box.Add(path_text,proportion = 5,flag = wx.EXPAND|wx.ALL,border = 3) # 添加组件
#proportion相对比例，flag：填充的样式和方向,wx.EXPAND为完整填充，wx.ALL为填充的方向，border：边框
box.Add(open_button,proportion = 2,flag = wx.EXPAND|wx.ALL,border = 3)
box.Add(save_button,proportion = 2,flag = wx.EXPAND|wx.ALL,border = 3)

v_box = wx.BoxSizer(wx.VERTICAL) # wx.VERTICAL参数表示实例化一个垂直尺寸器,比列是1：5
v_box.Add(box,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 3)
v_box.Add(content_text,proportion = 5,flag = wx.EXPAND|wx.ALL,border = 3)

v_box.Add(staic_text,proportion = 1,flag = wx.ALIGN_RIGHT| wx.ST_ELLIPSIZE_MIDDLE)
panel.SetSizer(v_box) # 设置主尺寸器
frame.Show()
app.MainLoop()
"""

#单选按钮RadioButton
"""
class RadionButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,title='Radio Example',size=(400, 300))
        self.InitUI()
    def InitUI(self):
        panel = wx.Panel(self)
        self.rb1 = wx.RadioButton(panel,11, label="vavel a", pos=(10, 10),style = wx.RB_GROUP)
        self.rb2 = wx.RadioButton(panel,22, label="vavel b", pos=(10, 40))
        self.rb3 = wx.RadioButton(panel,33, label="vavel c", pos=(10, 70))
        self.Bind(wx.EVT_RADIOBUTTON,self.OnRadiogroup)
        lblList = ['Value x','Value y','Value z']
        self.rbox = wx.RadioBox(panel,label = 'RadioBox',pos = (80,10),choices = lblList,
                                majorDimension = 1,style = wx.RA_SPECIFY_ROWS)
        self.rbox.Bind = (wx.EVT_RADIOBOX,self.onRadioBox)
        self.Centre()
        self.Show(True)

    def OnRadiogroup(self,e):
        rb = e.GetEventObject()
        print(rb.GetLabel(),'is clicked from Radio Group')
    def onRadioBox(self):
        print(self.rbox.GetStringSelection(),'is clicked from Radio Box')
ex = wx.App()
RadionButtonFrame()
ex.MainLoop()
"""

#复选框CheckBox
"""
class RadionButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,title='CheckBox Example',size=(400, 300))
        self.InitUI()
    def InitUI(self):
        panel = wx.Panel(self)
        self.cb1 = wx.CheckBox(panel, label="value a", pos=(10, 10))
        self.cb2 = wx.CheckBox(panel, label="value b", pos=(10, 40))
        self.cb3 = wx.CheckBox(panel, label="value c", pos=(10, 70))

        self.Bind(wx.EVT_CHECKBOX,self.onChecked)
        self.Centre()
        self.Show(True)

    def onChecked(self,e):
        cb = e.GetEventObject()
        print(cb.GetLabel(),'is clicked ',cb.GetValue)

ex = wx.App()
RadionButtonFrame()
ex.MainLoop()
"""


class RadionButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,title='CheckBox Example',size=(400, 300))
        panel = wx.Panel(self)
        box =wx.BoxSizer(wx.VERTICAL)
        self.label = wx.StaticText(panel,label = "your chioce",style = wx.ALIGN_CENTER)
        box.Add(self.Label,0,wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL,20)
        self.chlbl = wx.StaticText(panel,label = "choice control",style = wx.ALIGN_CENTER)
        box.Add(self.chlbl,0,wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL,5)
        path = "E:\git"
        dir = os.listdir(path)
        self.combo = wx.ComboBox(panel,choices = dir)
        box.Add(self.combo, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)


    def onChecked(self,e):
        cb = e.GetEventObject()
        print(cb.GetLabel(),'is clicked ',cb.GetValue)

ex = wx.App()
RadionButtonFrame()
ex.MainLoop()

path = "E:\git"
print(os.listdir(path))


# @classmethod



















