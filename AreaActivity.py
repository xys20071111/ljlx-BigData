import requests
import json,sys
from pyecharts.charts import Bar
from pyecharts import options as opts

AREAURL = 'http://eduyun.ljlx.com/appdata/stat/map?siteId={0}'
ACTIVITYURL = 'http://eduyun.ljlx.com/appdata/stat/mapDynamic?top={0}&siteId={1}'
SITEID = 'd43f1ff7-ae36-4b1e-9af8-98a9cf027c22'
COUNT = 1000

if len(sys.argv) == 2:
    SITEID = sys.argv[1]

areaData = requests.get(AREAURL.format(SITEID)).json()['data']
#print(areaData)
areaNameList = []
for v in areaData:
    areaNameList.append(v['areaName'])

userData = requests.get(ACTIVITYURL.format(COUNT,SITEID)).json()['data']
userActivity = {}
for v in areaNameList:
    userActivity[v] = 0
for v in userData:
    areaName = v['areaName']
    userActivity[areaName] = userActivity[areaName] + 1

activityList= []
for k,v in userActivity.items():
    print('{0}:{1}'.format(k,v))
    activityList.append(v)

chart = Bar()
chart.add_xaxis(areaNameList)
chart.add_yaxis('活跃度',activityList)
chart.set_global_opts(title_opts=opts.TitleOpts(title='乐教乐学瞬时活跃度'),xaxis_opts=opts.AxisOpts(name_rotate=60,axislabel_opts={"rotate":45,"interval":0}))
chart.render()
