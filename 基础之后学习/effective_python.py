#参考文档https://guoruibiao.gitbooks.io/effective-python/content/zun_xun_pep8_feng_ge_bian_cheng_feng_ge.html
#Pylint 是一个 Python 代码分析工具，它分析 Python 代码中的错误，查找不符合代码风格标准和有潜在问题的代码。
import time
def demo():
    a = 2
    if not a == 2:
        print('a')
    else:
        print('b')
if __name__ == '__main__':
    demo()
    print(time.time())
