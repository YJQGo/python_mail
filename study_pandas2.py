import pandas as pd
import matplotlib.pyplot as plt


# 填充缺失值
org_data = pd.read_csv('./csv_data/IMDB-Movie-Data.csv')
print(org_data.isna())
print(org_data)
# org_data.fillna('1',inplace=True)
# org_data.dropna(inplace=True)
# print(org_data.isna())
# print(org_data.head())
print(org_data)
org_data['Revenue (Millions)'].fillna(org_data['Revenue (Millions)'].mean(),inplace=True)
print(org_data)

