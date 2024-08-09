from collections import defaultdict
from tkinter import Image

import jieba
import numpy as np
from matplotlib import pyplot as plt
from wordcloud import WordCloud

path = ('C:\\Users\\Lenovo\\Downloads\\医院原始招标信息.xlsx')

import pandas as pd
df = pd.read_excel(path) # skiprows=2，不需要跳过任何行，第一行就是表头

dic = dict()
prices = defaultdict(list)

keys = ['视频', '移动', '便携式', '数字', '导', '通道', '动态']

r = ''
for index, row in df.iterrows():
    r = r + ',' + str(row[2].strip())


for key in keys:
    jieba.add_word(key)

stops = ['和', '术', '仪','脑电图仪','脑电图', '脑电','采集','图仪', '系统', '导脑电图仪','导脑','电图仪','集及','仪脑','测系统','集系统']
for stop in stops:
    jieba.del_word(stop)


result = jieba.lcut(r,cut_all=False)#全模式
print(result)
result1 = []
for i in result:
    if len(i) > 1:
        result1.append(i)

sentence=" ".join(result1)

words = WordCloud(font_path='msyh.ttc', background_color='white',width = 1000, height = 500,margin = 0, max_font_size=150,scale=20).generate(sentence)


plt.imshow(words) # 传入wordcloud对象
plt.axis('off') # 关闭坐标轴
plt.show() # 将图片展示出来