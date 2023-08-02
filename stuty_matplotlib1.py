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
plt.figure(figsize=(10, 8), dpi=100)

# 设置坐标轴刻度
plt.xticks(x_data[::3], x_lable[::3])
plt.yticks(range(35)[::3])
plt.grid(True, linestyle='--', alpha=0.5)

plt.xlabel("时间", fontsize=20)
plt.ylabel("温度")
plt.title("上海8月温度变化折线图")

# 绘制图像
plt.plot(x_data, shanghai_data, label="上海")
plt.plot(x_data, beijing_data, label="背景", color='r',linestyle='--')


plt.legend(loc=0)
plt.savefig('./zx.png')

# 展示图像
plt.show()
