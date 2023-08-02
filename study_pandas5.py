import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

pd.set_option('display.max_columns',None)

csv = pd.read_csv('./csv_data/IMDB-Movie-Data.csv')
print(csv)

or_genre = [i.split(',') for i in csv['Genre']]
unique_genre = pd.unique([i for j in or_genre for i in j])
print(unique_genre)

frame = pd.DataFrame(np.zeros([ csv.shape[0],unique_genre.shape[0]]), columns=unique_genre)


for row in range(1000):
    frame.loc[row,or_genre[row]] =1

frame.sum(axis=0).plot(kind='bar',figsize=(20,8))
plt.show()
# print(frame)

# print(frame)

# print(gere_zero)
# ser_genre = [i for i in temp_list for j in or_genre]
# print(ser_genre)
# pd.qcut(csv['Rating'], 10).value_counts().plot(kind='hist')
# plt.show()
# csv['Runtime (Minutes)'].plot(kind='hist',bins=20,figsize=(20,8))
# x_max = csv['Runtime (Minutes)'].max()
# x_min = csv['Runtime (Minutes)'].min()

# plt.xticks(np.linspace(x_min,x_max,21))
# plt.grid()
# plt.show()
# plt.show()
# csv['Rating'].qcut(100)
# print(csv['Director'].unique().shape[0])

# mean_data = csv['Rating'].groupby(csv['Title']).mean()

# print(mean_data)

