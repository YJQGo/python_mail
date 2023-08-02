import matplotlib.pyplot as plt
import pylab as mpl
import random

mpl.rcParams["font.sans-serif"] = ["SimHei"]

# 准备数据

x_data = range(30)
shanghai_data = [random.uniform(15, 35) for i in x_data]
beijing_data = [random.uniform(5, 15) for i in x_data]

x_lable = [f"第{i}天" for i in x_data]

# 创建画布
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8), dpi=100)

# 设置坐标轴刻度
axes[0].set_xticks(x_data[::3])
axes[0].set_xticklabels(x_lable[::3])
axes[0].set_yticks(range(35)[::3])
axes[0].set_xlabel("时间")
axes[0].set_ylabel("温度")
axes[0].grid(True,linestyle='--',alpha=0.5)
axes[0].set_title("上海8月温度变化折线图")



axes[1].set_xticks(x_data[::3])
axes[1].set_xticklabels(x_lable[::3])
axes[1].set_yticks(range(35)[::3])
axes[1].grid(True,linestyle='--',alpha=0.5)
axes[1].set_xlabel("时间")
axes[1].set_ylabel("温度")
axes[1].grid(True,linestyle='--',alpha=0.5)
axes[1].set_title("上海8月温度变化折线图")




# 绘制图像
axes[0].plot(x_data, shanghai_data, label="上海")
axes[1].plot(x_data, beijing_data, label="背景", color='r', linestyle='--')
axes[0].legend(loc=0)
axes[1].legend(loc=0)

# plt.savefig('./zx.png')

# 展示图像
plt.show()
