import numpy as np
import pandas as pd
import pandas.core.frame
import matplotlib.pyplot as plt

ori_data = pd.read_csv('./csv_data/链家北京租房数据.csv')

uni_data = ori_data.drop_duplicates()  #type:pd.core.frame.DataFrame
not_na_data = uni_data.dropna()
for index in not_na_data.index:
    area_str=not_na_data.loc[index,'面积(㎡)']
    not_na_data.loc[index, '面积(㎡)'] = area_str[:-2]
#     pass
#     # print(float(row[:-2]))
#     not_na_data.loc[index,'面积(㎡)'] = float(row[:-2])
#     print(not_na_data.loc[index])
huxing = []

for row in not_na_data['户型']:
    replace = row.replace('房间', '室')
    huxing.append(replace)

not_na_data['户型'] = huxing #type:pd.core.frame.DataFrame
#
# frame = pd.DataFrame({'区域': not_na_data['区域'].unique(), '数量': [0] * 13})
#
# frame['数量'] = not_na_data.groupby(by='区域')['户型'].count().values
# sort_house_count = frame.sort_values('数量',ascending=False)

#查看户型受欢迎程度 并画图表示
#
# def get_house_type(arr):
#     result = {}
#     keys = np.unique(arr)
#     for key in keys:
#         mask = (arr==key)
#         new_arr=arr[mask]
#         count = new_arr.size
#         result[key]=count
#     return result
#
#
# house_type = get_house_type(not_na_data['户型'])
#
# beyond_50_type = {x:y for x,y in house_type.items() if y>50}
#
# pd_house_type = pd.DataFrame({'户型': beyond_50_type.keys(), '数量': beyond_50_type.values()})
#
#
# plt.barh(pd_house_type['户型'],pd_house_type['数量'])
#
# for x, y in enumerate(beyond_50_type.values()):
#     print(f'{x}---{y}')
#     plt.text(y + 0.2, x - 0.1, '%s' % y)
#
# print(pd_house_type)
#
# plt.show()


print(not_na_data)

not_na_data['面积(㎡)'] = not_na_data['面积(㎡)'].astype(np.float32)

print(not_na_data['价格(元/月)'].div(not_na_data['面积(㎡)']))


# print(ori_data)
