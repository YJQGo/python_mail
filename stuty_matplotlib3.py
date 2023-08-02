import matplotlib.pyplot as plt
import pylab as mpl
import random

mpl.rcParams["font.sans-serif"] = ["SimHei"]

# 准备数据
# 0.准备数据
x_ticks=['雷神3：诸神⻩昏','正义联盟','东⽅快⻋谋杀案','寻梦环游记','全球⻛暴', '降魔传','追捕']
y_data=[73853,57767,22354,15969,14839,8725,8716]

# 创建画布
plt.figure(figsize=(20,8),dpi=100)

x = range(len(x_ticks))

# 绘制图像
plt.bar(x,y_data,width=0.5,color='r')

plt.xticks(x,x_ticks)

plt.grid(True,linestyle='--',alpha=0.5)

plt.title("票房数据柱状图")
# 展示图像
plt.show()