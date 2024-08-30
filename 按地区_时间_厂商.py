import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 假设你的Excel文件路径如下
file_path = 'C:\\Users\\Lenovo\\Downloads\\医院原始招标信息.xlsx'

# 读取Excel文件
df = pd.read_excel(file_path, parse_dates=['时间'])

# 确保时间字段是日期时间格式
df['时间'] = pd.to_datetime(df['时间'], errors='coerce')
# 只保留2015年及之后的数据
df = df[df['时间'].dt.year >= 2015]
df['年月'] = df['时间'].dt.to_period('Y')  # M是按照年月统计

df['中标供应商'] = df['中标供应商'].replace('', np.nan)  # 将空字符串替换为NaN
df = df.dropna(subset=['中标供应商'])  # 删除'厂商'列为NaN的所有行


jingjinji = ['北京', '天津', '河北']
df['地区'] = df['地区'].apply(lambda x: '京津冀' if x in jingjinji else x)
jiangzhehu = ['上海', '江苏', '浙江']
df['地区'] = df['地区'].apply(lambda x: '江浙沪' if x in jiangzhehu else x)
heijiliao = ['辽宁', '吉林', '黑龙江']
df['地区'] = df['地区'].apply(lambda x: '黑吉辽' if x in heijiliao else x)
xinan = ['重庆', '四川', '贵州', '云南', '西藏']
df['地区'] = df['地区'].apply(lambda x: '西南地区' if x in xinan else x)
huazhong = ['河南', '湖北', '湖南']
df['地区'] = df['地区'].apply(lambda x: '华中' if x in huazhong else x)
shanganning = ['陕西', '甘肃', '宁夏']
df['地区'] = df['地区'].apply(lambda x: '陕甘宁' if x in shanganning else x)
huanan = ['广东', '广西', '海南']
df['地区'] = df['地区'].apply(lambda x: '华南地区' if x in huanan else x)
huadong = ['安徽', '福建', '江西', '山东']
df['地区'] = df['地区'].apply(lambda x: '华东地区' if x in huadong else x)
others = ['山西', '内蒙', '青海']
df['地区'] = df['地区'].apply(lambda x: '其他' if x in others else x)


# 假设有一个DataFrame `market_share` 包含'地区'列
# 使用apply方法将所有不在特定地区列表中的地区标记为'其他'
vendors_to_keep = ['Natus', '日本光电', '博瑞康', '北京太阳', '上海诺诚', 'Cadwell', '北京新拓']  # 要保留的厂商列表

# 使用lambda表达式简化调整
df['厂商'] = df['中标供应商'].apply(lambda vendor: vendor if vendor in vendors_to_keep else '其他')



# 按照地区、中标供应商和年份进行分组计数
grouped = df.groupby([df['时间'].dt.year.rename('年月'), '地区', '厂商']).size().reset_index(name='中标次数')

# 对每个地区的中标次数进行汇总，以便计算占比
total_wins_per_year_region = grouped.groupby(['年月', '地区'])['中标次数'].sum().reset_index(name='总中标次数')

# 合并数据以计算市场占比
market_share = grouped.merge(total_wins_per_year_region, on=['年月', '地区'])
market_share['市场占比'] = market_share['中标次数'] / market_share['总中标次数']

# 绘制图表
markers = {'Natus': 'o', '日本光电': 's', '博瑞康': '*', '北京太阳': '^', '上海诺诚': 'D', 'Cadwell': ',', '北京新拓':'x', '其他': '*'}
colors = {'Natus': 'blue',
          '日本光电': 'red',
          '博瑞康': 'green',
          '北京太阳': 'purple',
          '上海诺诚': 'orange',
          'Cadwell': 'brown',
          '北京新拓': 'yellow',
          '其他': 'gray'}
for region in market_share['地区'].unique():
    # 提取特定地区的数据
    region_data = market_share[market_share['地区'] == region]

    # 创建一个新的图表
    plt.figure(figsize=(10, 5))
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示问题
    plt.rcParams['axes.unicode_minus'] = False  # 解决中文显示问题
    plt.title(f'{region} 中标供应商市场占比随年份变化')
    plt.xlabel('年份')
    plt.ylabel('市场占比')

    # 为每个供应商绘制一条线
    for supplier in region_data['厂商'].unique():
        supplier_data = region_data[region_data['厂商'] == supplier]
        plt.plot(supplier_data['年月'], supplier_data['市场占比'], marker=markers[supplier], color=colors[supplier], linestyle='-', label=supplier)

    # 添加图例
    plt.legend(title='中标供应商')

    # 显示图表
    plt.show()