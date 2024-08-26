import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取Excel文件
df = pd.read_excel('C:\\Users\\Lenovo\\Downloads\\医院原始招标信息.xlsx', engine='openpyxl')

# 将时间列转换为日期时间类型
df['招标时间'] = pd.to_datetime(df['招标时间'])

# 提取年份
df['年份'] = df['招标时间'].dt.year
df = df[df['招标时间'] >= '2015-01-01'] # 去除2015以前的数据

# print(df)
vendors_to_keep = ['Natus', '日本光电', '博瑞康', '北京太阳', '上海诺诚', 'Cadwell']  # 要保留的厂商列表

# 使用lambda表达式简化调整
df['厂商'] = df['中标供应商'].apply(lambda vendor: vendor if vendor in vendors_to_keep else '其他')

# 输出调整后的DataFrame
print(df)


# 按年份和厂商分组，计算每个厂商在每年的数量
grouped_by_year = df.groupby(['年份', '厂商']).size().reset_index(name='数量')
# print(grouped_by_year)
#
# 计算每个年份的总数量
yearly_totals = grouped_by_year.groupby('年份')['数量'].sum().reset_index(name='年总量')
# print(yearly_totals)
#
# 合并数据以计算占比
market_share = grouped_by_year.merge(yearly_totals, on='年份')
market_share['占比'] = market_share['数量'] / market_share['年总量']
print(market_share)
#
# 绘制趋势图
plt.figure(figsize=(12, 6))
sns.lineplot(data=market_share, x='年份', y='占比', hue='厂商', marker='o')
plt.rcParams['font.sans-serif'] = ['SimHei']   #解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False    # 解决中文显示问题
# 设置图表标题和标签
plt.title('厂商市场份额随年份变化趋势')
plt.xlabel('年份')
plt.ylabel('市场占比')
plt.legend(title='厂商')

# 显示图表
plt.show()