from collections import defaultdict
import pandas as pd
from matplotlib import pyplot as plt

path = ('C:\\Users\\Lenovo\\Downloads\\医院原始招标信息.xlsx')

from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]

df = pd.read_excel(path) # skiprows=2，不需要跳过任何行，第一行就是表头

times = []
values = defaultdict(list)
# for index, row in df.iterrows():
#     # print(row['招标时间'])
#     if row['通道数'] == 32:
#         print(row['招标时间'],row['单价金额万（成交金额，最高限价）'])
#         t = row['招标时间'].strftime("%Y-%m")
#         plt.scatter(t, row['单价金额万（成交金额，最高限价）'], alpha=0.8, c='b')
#
#
# plt.title('32通道脑电图仪价格')
# plt.xlabel('时间（年-月）')  # 横坐标轴标题
# plt.ylabel('金额（万）')  # 纵坐标轴标题
# plt.show()

# for index, row in df.iterrows():
#     t = row['招标时间'].strftime("%Y-%m")
#     plt.scatter(t, row['单价金额万（成交金额，最高限价）'], alpha=0.8, c='g')
#
#
# plt.title('所有脑电图仪价格')
# plt.xlabel('时间（年-月）')  # 横坐标轴标题
# plt.ylabel('金额（万）', rotation='vertical')  # 纵坐标轴标题
# plt.xticks(rotation=90)
# plt.show()

for index, row in df.iterrows():
    t = row['招标时间'].strftime("%Y")
    plt.scatter(t, row['单价金额万（成交金额，最高限价）'], alpha=0.8, c='g')


plt.title('所有脑电图仪价格')
plt.xlabel('时间（年-月）')  # 横坐标轴标题
plt.ylabel('金额（万）', rotation='vertical')  # 纵坐标轴标题
plt.xticks(rotation=90)
plt.show()