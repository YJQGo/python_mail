import numpy as np
import matplotlib.pyplot as plt

# 生成正态分布和均匀分布并画出直方图


uniform = np.random.uniform(0, 10, 20)

print(uniform)

reshape = uniform.reshape([-1, 10])
print(reshape)
uniform.resize([10,2])
print(uniform)

print(uniform.T)

print(uniform.astype(np.int32))
# print(uniform.tostring())

print(np.unique(uniform))