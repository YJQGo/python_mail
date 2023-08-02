import pandas as pd

csv_data = pd.read_csv('./csv_data/iris.csv')
removed_data = csv_data.drop('Species',axis=1)

print(csv_data.sort_values(by='Sepal.Length',ascending=False))

# print(f'数据类型为{removed_data.dtype}')

print('-----------------------------------')

# print(csv_data[][1])




