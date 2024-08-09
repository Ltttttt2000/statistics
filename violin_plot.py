import matplotlib.pyplot as plt
import numpy as np

from collections import defaultdict

path = ('C:\\Users\\Lenovo\\Downloads\\医院原始招标信息.xlsx')

import pandas as pd
df = pd.read_excel(path) # skiprows=2，不需要跳过任何行，第一行就是表头

prices = []

for index, row in df.iterrows():
    if pd.isna(row[4]) is False:
        prices.append(row[4])


import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'simhei'
plt.rcParams['axes.unicode_minus'] = False

data = prices

plt.title("价格分布")
plt.violinplot(data, showmeans=True)
plt.ylabel('万元')
plt.tight_layout()
plt.show()
