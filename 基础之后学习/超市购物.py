import pandas as pd
import numpy as np

#http://www.ocrmaker.com/  #读取图片文字
class ShopManager(object):
    # path:表示读取文件的路径    shopdic：表示存放内存的容器
    # def __init__(self,path):
    #    self.path = path
    #    self.shopdic = self.readFileToDic()
    def admin_readxls(self):
        df = pd.read_excel("shop.xls")
        sale,cout = self.userwork()
        df1 = df[df['商品名称'].str.contains(sale)]   #筛选excel，商品名称列中筛选带有'西服'的数据
        df['数量'][df['商品名称'] == sale] -= int(cout) #数量+值
        df.to_excel("shop.xls", sheet_name='shop', index=False, header=True) #写入表格
        # print(df[['商品名称', '价格', '数量']])
    def user_readxls(self):
        df = pd.read_excel("shop.xls")
        print('好嗨百货公司商品')
        print(df[['商品名称','价格','数量']])
    def adminwork(self):
        df = pd.read_excel("shop.xls")
        print(df[['商品名称', '价格', '数量']])
    def userwork(self):
        self.user_readxls()
        while True:
            buy = input("选择你购买商品名称 无需购物请按n键退出：")
            count = input("选择你购买商品数量：")
            if buy == 'n':
                print("退出购物")
                break
            if not buy == None:
                if not count == None:
                    print("购物愉快")
                    df = pd.read_excel("shop.xls")
                    df1 = df[df['商品名称'].str.contains(buy)]  # 筛选excel，商品名称列中筛选带有'西服'的数据
                    df['数量'][df['商品名称'] == buy] -= int(count)  # 数量+值
                    df.to_excel("shop.xls", sheet_name='shop', index=False, header=True)  # 写入表格
            else:
                print("请美女选择购买商品")
    def login(self):
        print("欢迎进入好嗨超市")
        username = input('请输入用户名:')
        password = input('请输入密码:')
        if username == "admin":
            if password =='123':
                print("欢迎你老板")
                self.adminwork()
            else:
                print('老板你密码错误')
        else:
            print("欢迎你%s美女"%username)
            self.userwork()
if __name__ == '__main__':
    sh = ShopManager()
    sh.login()

