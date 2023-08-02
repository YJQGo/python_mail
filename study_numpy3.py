import numpy as np
import matplotlib.pyplot as plt

#生成正态分布和均匀分布并画出直方图


normal = np.random.normal(0, 1, 100000)

uniform = np.random.uniform(2, 10, 10000000)

print(uniform)

plt.figure(figsize=(10,5),dpi=100)

plt.hist(uniform,1000)

plt.show()