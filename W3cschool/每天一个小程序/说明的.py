# zidian={'刘强东':'46','章泽天':'36','周杰伦':'40','昆凌':'26'}
# for k ,v in zidian.items():
#     print(k,v)

import pandas as pd

def zhuabao():
    url_df = pd.DataFrame({'urls':['http://www.cbooo.cn/BoxOffice/getWeekInfoData?sdate=' for i in range(5)],'date' :pd.date_range(20190114,freq = 'W-MON',periods = 5)})

    '''
    将网址相同的部分生成5次，并利用pandas的时间序列功能生成5个星期一对应的日期。
    其中用到了第一部分提供的多个数据类型：
    range(5)属于列表，
    'urls'：[]属于字典，
    pd.dataframe属于dataframe
    '''
    url_df['urls'] = url_df['urls'] + url_df['date'].astype('str')
    print(url_df)
def fenxi():
    data = pd.read_csv('中国票房数据爬取测试20071-20192.csv', engine='python')
    #data[data['平均上座人数'] > 20]['电影名']
    # 计算周票房第一随时间变化的结果，导入数据，并选择平均上座人数在20以上的电影为有效数据

    dataTop1_week = data[data['排名'] == 1][['电影名', '周票房']]
    # 取出周票房排名为第一名的所有数据，并保留“电影名”和“周票房”两列数据

    dataTop1_week = dataTop1_week.groupby('电影名').max()['周票房'].reset_index()
    # 用“电影名”来分组数据，相同电影连续霸榜的选择最大的周票房保留，其他数据删除

    dataTop1_week = dataTop1_week.sort_values(by='周票房', ascending=False)
    # 将数据按照“周票房”进行降序排序

    dataTop1_week.index = dataTop1_week['电影名']
    del dataTop1_week['电影名']
    # 整理index列，使之变为电影名，并删掉原来的电影名列
    print(dataTop1_week)
    # 查看数据
#fenxi()