import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('C:\\Users\\Lenovo\\Downloads\\医院原始招标信息.xlsx')

# 计算每个城市中标最多的供应商
max_suppliers = df.groupby('地区')['中标供应商'].value_counts().groupby(level=0).idxmax()
max_suppliers_df = max_suppliers.to_frame(name='计数').reset_index()

# 只保留中标供应商这一列和城市信息
max_suppliers_df = max_suppliers_df[['地区', '中标供应商']]

# 假设有一个包含中国省份边界的Shapefile文件
# 这个文件可以从多个来源下载，例如GADM (http://gadm.org/)
# 假设Shapefile文件已下载并存放在指定路径下
china_map = gpd.read_file('path/to/china_provinces.shp')

# 假设china_map中有一个名为'NAME_1'的字段，代表省份名
# 将'城市'列与'NAME_1'进行匹配
# 注意实际操作时可能需要根据具体情况调整字段名
# 此处假设'城市'与'NAME_1'完全匹配
merged_data = china_map.merge(max_suppliers_df, left_on='NAME_1', right_on='城市', how='left')

# 处理未匹配到的城市
# 使用fillna来填充未匹配到的城市，这里可以用一个默认值来表示未匹配到的情况
merged_data['中标供应商'] = merged_data['中标供应商'].fillna('未知供应商')

# 绘制地图
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_data.plot(column='中标供应商', categorical=True, legend=True, ax=ax)
ax.set_title('主导供应商按地区分布')
plt.show()