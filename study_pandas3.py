import pandas
import pandas as pd

stock_data= pd.read_csv("./csv_data/stock_day.csv")
print(stock_data)
qcut = pd.qcut(stock_data['price_change'], 10)

print(qcut.value_counts())

pd.set_option('display.max_columns', None)
cut = pd.cut(stock_data['price_change'], bins=[-100, -7, -5, -3, 0, 3, 5, 7, 100])
dummies = pandas.get_dummies(cut, prefix='rise')
print(dummies)


