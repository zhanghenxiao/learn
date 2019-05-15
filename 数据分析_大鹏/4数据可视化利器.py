# -*- coding: utf-8 -*-
# @File    : 数据可视化利器.py  交互图表
# @Date    : 2019-05-13
# @Author  : Zhang.Cookie
#参考链接：https://www.kesci.com/home/project/5cd9258f0ee9cd002ccada56

# 阿里大屏Datav 逼格高
# d3，infogram，echat(单r张图)
#https://pyecharts.org/#/ 官方文档

from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType
# 导入主题：https://pyecharts.org/#/zh-cn/themes
# .LIGHT、.DARK、.CHALK、.ESSOS、.INFOGRAPHIC、.PURPLE_PASSION ...
from pyecharts.charts import Bar

#柱状图
def shangjia():
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    # 创建变量数据

    bar = (
        Bar(opts.InitOpts(width='1000px', height='500px', theme=ThemeType.INFOGRAPHIC)) #图表画布宽度，高度，图表主题
            .add_xaxis(x)
            .add_yaxis("商家A", v1, is_selected=True)  #图例配置项
            .add_yaxis("商家B", v2, is_selected=True)
            .set_global_opts(
            # 设置全局参数
            title_opts=opts.TitleOpts(title="商场数据显示"),  # 设置title
            xaxis_opts=opts.AxisOpts(
                splitline_opts=opts.SplitLineOpts(is_show=True)
            ),  # 设置x轴
            yaxis_opts=opts.AxisOpts(
                splitarea_opts=opts.SplitAreaOpts(is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1))
            ),  # 设置y轴
            toolbox_opts=opts.ToolboxOpts(is_show=True),  # 设置工具箱
            datazoom_opts=[opts.DataZoomOpts(range_start=10, range_end=80, is_zoom_lock=False)],  # 设置区域缩放配置slider
        )
            .set_series_opts(
            # 设置系列配置，标记点数据项
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[
                    opts.MarkLineItem(type_="average", name="平均值"),
                ]
            ),
        )
    )

    bar.render('C:\\Users\\succful\\Desktop\\opencvStudy\\数据分析_大鹏\\shangjia.html') #保存
#折线图
def zhe():
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    line = (
        Line(opts.InitOpts(width='1000px', height='500px'))
            .add_xaxis(x)
            .add_yaxis("商家A", v1, is_selected=True, is_smooth=True)
            .add_yaxis("商家B", v2, is_selected=True, is_step=True)
    )
    line.render('C:\\Users\\succful\\Desktop\\opencvStudy\\数据分析_大鹏\\zhe.html')
zhe()
