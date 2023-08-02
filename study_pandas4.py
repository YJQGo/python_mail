import matplotlib.pyplot as plt
import pandas as pd

# 分组聚合案例
pd.set_option('display.max_columns',None)
xbk_local_data = pd.read_csv('./csv_data/directory.csv')
print(xbk_local_data)
group_country = xbk_local_data.groupby(['Country','State/Province']).count()

print(group_country)
# group_country['Brand'].plot(kind='bar',figsize=(20,8))
# plt.show()