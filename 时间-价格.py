import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_and_process_data(file_path):
    """
    加载数据并进行必要的预处理。
    :param file_path: 数据文件路径
    :return: 处理后的 DataFrame
    """
    # 读取 CSV 文件
    data = pd.read_excel(file_path)

    # 将时间字符串转换为日期时间对象
    data['Time'] = pd.to_datetime(data['时间'])

    # 提取年份和月份
    data['Year'] = data['时间'].dt.year
    data['Month'] = data['时间'].dt.month

    # 创建年月组合字段
    data['YearMonth'] = data['时间'].dt.strftime('%Y-%m')

    # 按照 YearMonth 排序
    data.sort_values(by='YearMonth', inplace=True)
    data.dropna(subset=['通道数'], inplace=True)
    data['通道数'] = data['通道数'].astype(int)

    return data


def plot_price_trend(data):
    """
    绘制按时间和通道数的价格变化趋势图。
    :param data: 包含数据的 DataFrame
    """
    # 分组并计算每个月每个通道数的平均价格
    grouped_data = data.groupby(['YearMonth', '通道数'])['价格'].mean().reset_index()
    # 设置图形大小
    plt.figure(figsize=(14, 7))

    # 使用 Seaborn 绘制线图
    sns.lineplot(x='YearMonth', y='价格', hue='通道数', data=grouped_data,
                 palette="tab10", marker='o', markersize=10, linewidth=2.5)

    # 设置图表标题和轴标签
    plt.title('Average Price Change by Month for Different Channel Numbers')
    plt.xlabel('Month')
    plt.xticks(rotation=45)  # 旋转 x 轴标签以避免重叠
    plt.ylabel('Average Price')

    # 添加图例
    plt.legend(title='Channel Number')

    # 显示图表
    plt.show()


# 主程序入口
if __name__ == "__main__":
    # 指定 CSV 文件路径
    file_path = 'C:\\Users\\Lenovo\\Downloads\\医院原始招标信息.xlsx'

    # 加载并处理数据
    processed_data = load_and_process_data(file_path)

    # 绘制价格趋势图
    plot_price_trend(processed_data)