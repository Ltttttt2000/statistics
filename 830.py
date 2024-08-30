import collections
from collections import defaultdict

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def manufacture_pie(excel_file):
    df = pd.read_excel(excel_file)

    specific_manufacture = ['Natus', '日本光电', '北京新拓', '博瑞康', '北京太阳', '上海诺诚', 'Cadwell', '德力凯', '江西诺诚', '意大利 EB NEURO', 'Compumedics'] # '北京云深', '迈联' '河南美伦', '共同医疗'
    df['中标供应商'] = df['中标供应商'].apply(lambda x: '其他' if x not in specific_manufacture else x)


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
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示问题
    plt.rcParams['axes.unicode_minus'] = False  # 解决中文显示问题
    fig, ax = plt.subplots()
    patches, texts, autotexts = plt.pie(all_area.values(), labels=all_area.keys(), autopct='%1.1f%%', pctdistance=0.8, startangle=140, textprops={'fontsize': 8})

    # 调整标签位置
    for text in texts:
        text.set_fontsize(10)
    plt.title('全部的中标厂商分布')
    plt.show()

def count_suppliers(excel_file):
    # 读取 Excel 文件
    df = pd.read_excel(excel_file)

    # 计算每个供应商的出现次数
    supplier_counts = df['中标供应商'].value_counts()

    # 将结果保存到新的 Excel 文件
    supplier_counts.to_excel('supplier_counts.xlsx')

    return supplier_counts


def plot_supplier_counts(excel_file):
    # 读取 Excel 文件
    df = pd.read_excel(excel_file)

    # 计算每个供应商的出现次数
    supplier_counts = df['中标供应商'].value_counts()

    # 绘制条形图
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示问题
    plt.rcParams['axes.unicode_minus'] = False  # 解决中文显示问题
    supplier_counts.plot(kind='bar', title='供应商出现次数')
    plt.xlabel('中标供应商')
    plt.ylabel('出现次数')
    plt.xticks(rotation=45)  # 旋转 x 轴标签以便更好地显示
    plt.tight_layout()  # 自动调整子图参数以使子图适合图形区域
    plt.show()


def plot_horizontal_bar_chart(excel_file):
    # 加载数据
    df = pd.read_excel(excel_file)  # 假设Excel文件名为'hospital_data.xlsx'

    # 计算每个中标供应商的出现次数
    supplier_counts = df['中标供应商'].value_counts()

    # 创建一个新的图形
    plt.figure(figsize=(12, 8))

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示问题
    plt.rcParams['axes.unicode_minus'] = False  # 解决中文显示问题
    # 绘制垂直条形图
    # 绘制水平条形图

    # 按值降序排序
    sorted_supplier_counts = supplier_counts.sort_values(ascending=True)

    # 绘制水平条形图
    bars = plt.barh(sorted_supplier_counts.index, sorted_supplier_counts.values, color='skyblue')


    # 添加每个条形上的数值
    for index, value in enumerate(sorted_supplier_counts.values):
        plt.text(value, index, str(value), va='center')

    # 设置图表标题和坐标轴标签
    plt.title('全球2015-2024年脑电图仪中标供应商的统计次数')
    plt.xlabel('中标次数')
    plt.ylabel('中标供应商')
    plt.tight_layout()  # 自动调整子图布局
    plt.show()


if __name__ == "__main__":
    # 指定 Excel 文件路径
    excel_file = 'C:\\Users\\Lenovo\\Downloads\\医院原始招标信息.xlsx'
    # 计算供应商出现次数并画图
    supplier_counts = count_suppliers(excel_file)
    print(supplier_counts)
    #
    # # 供应商的次数条形图
    # plot_horizontal_bar_chart(excel_file)

    # 供应商分布
    manufacture_pie(excel_file)


