import sys
#from PyQt4 import QtGui,QtCore #(动作)
from PyQt4 import QtGui,QtCore

# app = QtGui.QApplication(sys.argv)
# widget = QtGui.QWidget()    #生成一个对象
# widget.resize(300,200)      #窗口大小
# widget.setWindowTitle("test")
# widget.show()
# sys.exit(app.exec_())

# class three_close(QtGui.QWidget):
#     def __init__(self,parent = None):
#         QtGui.QWidget.__init__(self)
#         self.setGeometry(300,300,350,250) #x,y坐标，窗口大小
#         self.setWindowTitle(u'小提示')
#         quit = QtGui.QPushButton(u'关闭',self)     #光比窗口
#         quit.setGeometry(280,200,60,35)
#         self.connect(quit,QtCore.SIGNAL('clicked()'),QtGui.qApp,QtCore.SLOT('quit()'))
# app = QtGui.QApplication(sys.argv)
# tooltip = three_close()
# tooltip.show()
# sys.exit(app.exec_())

# class five_tool(QtGui.QMainWindow):    #窗口菜单栏和工具栏的使用（）
#     def __init__(self,parent = None):
#         QtGui.QMainWindow.__init__(self)
#         self.resize(550,450)
#         self.setWindowTitle(u'我的小程序')
#
#         testedit = QtGui.QTextEdit()   #编辑成功
#         self.setCentralWidget(testedit)
#
#         exit = QtGui.QAction(QtGui.QIcon('exit.png'),u'退出',self)
#         exit.setShortcut('Ctrl+Q')
#         exit.setStatusTip(u'退出程序')
#         exit.connect(exit,QtCore.SIGNAL('triggerd()'),QtGui.qApp,QtCore.SLOT('quit()'))
#
#         self.statusBar()
#         menubar = self.menuBar()
#         file = menubar.addMenu(u'文件')
#         file.addAction(exit)
#
# app = QtGui.QApplication(sys.argv)
# tooltip = five_tool()
# tooltip.show()
# sys.exit(app.exec_())

# class six_Boxlayout(QtGui.QWidget):  #BOX布局
#     def __init__(self, parent=None):
#         QtGui.QWidget.__init__(self)
#         self.setWindowTitle(u'Box布局')
#
#         sure = QtGui.QPushButton(u'确定')
#         cancel = QtGui.QPushButton(u'返回')
#         self.connect(cancel, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))
#
#         hbox = QtGui.QHBoxLayout()  #此乃水平布局
#         hbox.addStretch(1)      #增加一个界面
#         hbox.addWidget(sure)
#         hbox.addWidget(cancel)
#
#         vbox = QtGui.QVBoxLayout()  #此乃垂直布局
#         vbox.addStretch(1)
#         vbox.addLayout(hbox)
#
#         self.setLayout(vbox)  #镶嵌界面
#
#         self.resize(400,250)
#
# app = QtGui.QApplication(sys.argv)
# tooltip = six_Boxlayout()
# tooltip.show()
# sys.exit(app.exec_())

# class six_Grildlayout(QtGui.QWidget):  #网格布局
#     def __init__(self, parent=None):
#         QtGui.QWidget.__init__(self)
#         self.setWindowTitle(u'计算器布局图')
#         names = ['7','8','9','*','4','5','6','-','1','2','3','+','','',u'确定',u'取消']
#         grid = QtGui.QGridLayout()  #创建一个网格布局对象
#
#         j = 0
#         pos = [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3),(4,0),(4,1),(4,2),(4,3)]
#         for i in names:
#             button = QtGui.QPushButton(i)
#             if j == 11 and j ==12:
#                 grid.addWidget(QtGui.QLabel(''),4,0)  #指定网格坐标，让其空白
#                 grid.addWidget(QtGui.QLabel(''),4,1)
#             else:
#                 grid.addWidget(button,pos[j][0],pos[j][1])
#             j += 1
#         self.setLayout(grid)
#
# app = QtGui.QApplication(sys.argv)
# tooltip = six_Grildlayout()
# tooltip.show()
# sys.exit(app.exec_())

# class seven_SigSlot(QtGui.QWidget):  #滑动块测试
#     def __init__(self, parent=None):
#         QtGui.QWidget.__init__(self)
#         self.setWindowTitle(u'滑动块测试')
#
#         lcd = QtGui.QLCDNumber(self)
#         slider = QtGui.QSlider(QtCore.Qt.Horizontal,self)
#
#         vbox = QtGui.QVBoxLayout()
#         vbox.addWidget(lcd)
#         vbox.addWidget(slider)
#
#         self.setLayout(vbox)
#         self.connect(slider,QtCore.SIGNAL('valueChanged(int)'),lcd,QtCore.SLOT('display(int)'))
#         self.resize(550,450)
#         self.connect(self,QtCore.SIGNAL('closeEmitAPP()'),QtCore.SLOT('close()'))   #对事件进行处理
#
#     def keyPressEvent(self,event):
#         if event.key() == QtCore.Qt.Key_Escape:
#             self.close()
# app = QtGui.QApplication(sys.argv)
# tooltip = seven_SigSlot()
# tooltip.show()
# sys.exit(app.exec_())

# class seven_Esc(QtGui.QWidget):  #按住esc键关闭程序
#     def __init__(self, parent=None):
#         QtGui.QWidget.__init__(self)
#         self.setWindowTitle(u'按住esc键关闭程序')
#         self.setGeometry(550,450,550,450)  #根据坐标显示窗口
#         self.resize(550, 450)  #默认居中
#         self.connect(self,QtCore.SIGNAL('closeEmitAPP()'),QtCore.SLOT('close()'))   #对事件进行处理
#         self.resize(550,450)
#     def keyPressEvent(self,event):
#         if event.key() == QtCore.Qt.Key_Escape:
#             self.close()
#
# app = QtGui.QApplication(sys.argv)
# tooltip = seven_Esc()
# tooltip.show()
# sys.exit(app.exec_())

class eghit_Openfile(QtGui.QMainWindow):  #打开文件夹
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle(u'打开文件夹')
        self.resize(550,450)   #默认居中
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        self.setFocus()   #设置焦点

        open = QtGui.QAction(QtGui.QIcon('open.ico'),u'打开',self)
        open.setShortcut('Ctrl+O')
        open.setStatusTip(u'打开新文件')
        self.connect(open,QtCore.SIGNAL('triggered()'),self.showDialog)   #对事件进行处理

        menubar = self.menuBar()
        file = menubar.addMenu('&file')
        file.addAction(open)

    def showDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self,u'文件夹','./')
        file = open(filename)
        data = file.read()
        self.textEdit.setText(data)
app = QtGui.QApplication(sys.argv)
tooltip = eghit_Openfile()
tooltip.show()
sys.exit(app.exec_())

















































