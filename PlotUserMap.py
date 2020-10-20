from pyecharts.charts import Bar
from pyecharts import options as opts
import requests
data = requests.get('http://eduyun.ljlx.com/appdata/stat/map?siteId=d43f1ff7-ae36-4b1e-9af8-98a9cf027c22').json()['data']
areaNameList = []
areaSchoolCount = []
areaClassCount = []
for v in data:
    areaNameList.append(v['areaName'])
    areaSchoolCount.append(v['schoolCount'])
    areaClassCount.append(v['classCount'])
#print(areaNameList)
schoolCountChart = Bar()
schoolCountChart.add_xaxis(areaNameList)
schoolCountChart.add_yaxis('学校数',areaSchoolCount,bar_max_width=10000)
schoolCountChart.add_yaxis('班级数',areaClassCount)
schoolCountChart.set_global_opts(title_opts=opts.TitleOpts(title='乐教乐学学校数量图'))
schoolCountChart.render()