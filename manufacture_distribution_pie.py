'''
画地区分布的饼图
matplotlib.pyplot.pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=0, radius=1, counterclock=True, wedgeprops=None, textprops=None, center=0, 0, frame=False, rotatelabels=False, *, normalize=None, data=None)[source]
'''
import collections
import os
from collections import defaultdict

import pandas as pd

path = ('C:\\Users\\Lenovo\\Downloads\\医院原始招标信息.xlsx')

import pandas as pd
df = pd.read_excel(path) # skiprows=2，不需要跳过任何行，第一行就是表头
dic = defaultdict(list)
all_manufacture = []
for index, row in df.iterrows():
    manufacture = row['中标供应商']
    area = row['地区']

    if pd.isna(row["中标供应商"]) is False:
        manufacture = str(row['中标供应商'])
        dic[area].append(manufacture)
        all_manufacture.append(manufacture)


all_area = collections.Counter(all_manufacture)
jiangzhehu = collections.Counter(dic['江浙沪'])
jingjinji = collections.Counter(dic['京津冀'])
guangdong = collections.Counter(dic['广东'])
xinjiang = collections.Counter(dic['新疆'])

# print(guangdong.keys(), guangdong.values())
# print(guangdong)


import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']   #解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False    # 解决中文显示问题

plt.pie(all_area.values(), labels=all_area.keys(), autopct='%.2f%%', pctdistance=0.8, textprops={'fontsize': 8})
plt.title('全部的中标厂商分布')


# plt.figure(figsize=(20, 20))
#
# plt.subplot(221)
# plt.pie(jingjinji.values(), labels=jingjinji.keys(), autopct='%.2f%%', pctdistance=0.8, textprops={'fontsize': 8})
# plt.title('京津冀地区中标厂商分布')
#
# plt.subplot(222)
# plt.pie(jiangzhehu.values(), labels=jiangzhehu.keys(), autopct='%.2f%%', pctdistance=0.8, textprops={'fontsize': 8})
# plt.title('江浙沪地区中标厂商分布')
#
# plt.subplot(223)
# plt.pie(guangdong.values(), labels=guangdong.keys(), autopct='%.2f%%', pctdistance=0.8, textprops={'fontsize': 8})
# plt.title('广东地区中标厂商分布')
#
# plt.subplot(224)
# plt.pie(xinjiang.values(), labels=xinjiang.keys(), autopct='%.2f%%', pctdistance=0.8, textprops={'fontsize': 8})
# plt.title('新疆地区中标厂商分布')
plt.show()




