import pandas as pd
import matplotlib.pyplot as plt

csv_data = pd.read_csv('./csv_data/stock_day.csv').drop(['ma5','ma10','ma20','v_ma5','v_ma10','v_ma20','turnover'],axis=1)

# print(csv_data)
# print(csv_data.set_index(['open']))

# csv_data.to_csv('./write.csv')
csv_data.to_json("./data_json.json",orient='records',lines=True)



# date_up[]
# print(apply)

# print(csv_data.reset_index())
# print(csv_data.head())

csv_data



