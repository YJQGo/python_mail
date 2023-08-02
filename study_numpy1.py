import numpy as np
import time
import random


list = []

for i in range(100000000):
    random_num = random.random()
    list.append(random_num)
start1 = time.time()
sum_list = sum(list)
end1 = time.time()

print(end1-start1)

array = np.array(list)
start2 = time.time()
array = np.sum(array)
end2 = time.time()

print(end2-start2)
