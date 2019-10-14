#参考文档https://guoruibiao.gitbooks.io/effective-python/content/zun_xun_pep8_feng_ge_bian_cheng_feng_ge.html
#Pylint 是一个 Python 代码分析工具，它分析 Python 代码中的错误，查找不符合代码风格标准和有潜在问题的代码。
import time
import pyautogui
import base64
#not语法
def demo():
    a = 2
    if not a == 2:
        print('a')
    else:
        print('b')
#文字写入txt
def with_test():
    with open("收盘价Dashboard.html", 'a', encoding='utf-8') as html_file:
        html_file.write('收盘价Dashboard charset = "utf-8" >\n')
        txtlist = ['收盘折线图.svg', '收盘价对数变换折线图.svg',
                    '收盘价月日均收益￥.svg',
                    '收盘价周日均值￥.svg', "收盘价星期均值￥.svg"]
        for svg in txtlist:
            with open(svg, 'rb') as f:
                bian_ma = base64.b64encode(f.read())
                message = '<img src="data:image/png;base64,' + str(bian_ma, encoding='utf-8') + '"/>'
                with open('a.html', 'w') as f3:
                    f3.write(message)
#图片写入HTML
def image_html():
    with open(r'two.png', 'rb') as f:
        bian_ma = base64.b64encode(f.read())

    # imagedata = base64.b64decode(bian_ma)
    # with open('one.jpg', "wb") as f:
    #     file.write(imagedata)

    # message='<img src="data:image/png;base64,'+ bian_ma +'"/>'  #注意bytes 和str的区别
    message ='<img src="data:image/png;base64,'+str(bian_ma,encoding = 'utf-8') +'"/>'  #图片写入html中
    with open('a.html', 'w') as f3:
        f3.write(message)
#监控按键貌似鼠标监控不了
def rightclick():
    from pynput.keyboard import Listener
    import logging

    wenjianweizhi = "C:\\Users\\succful\\Desktop\\opencvStudy\\基础之后学习\\"
    logging.basicConfig(filename=(wenjianweizhi + "keylogger.txt"), format="%(asctime)s:%(message)s",
                        level=logging.DEBUG)
    def press(key):
        logging.info(key)

    with Listener(on_press=press) as listener:
        listener.join()
    pyautogui.click(button="right")  # 右击
# 如何将df的数据进行合并
def data_df():
    import pandas as pd
    key = pd.DataFrame(
        data={
            'user': [18, 18, 18, 19, 19],
            'name': ['江苏', '四川', '北京', '成都', '天津']
        })
    key = key.groupby('user')['name'].apply(lambda x: ",".join(map(lambda x: "'%s'" % x, x))).reset_index()  #以实现效果
#sys.append()导入自定义模块的时候出错
def sys_insert():
    #在终端运行
    import sys
    sys.path.append('D\python')
#pycharm 打开摄像头
def cv_opencamera():
    import cv2
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    data_df()
