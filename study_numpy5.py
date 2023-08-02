import random

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

student_score = np.random.randint(40, 100, (10, 5))
print(student_score)

col_name=['语文','数学','英语','政治','408计算机基础']
row_name = ['学生'+str(i+1) for i in range(student_score.shape[0])]


frame = pd.DataFrame(student_score,columns=col_name,index=row_name)

print(f'shape为{frame.shape}')
print(f'values为{frame.values}')
print(f'index为{frame.index}')
print(f'columns{frame.columns}')

print(f'前3行{frame.head(3)}')
print(f'后2行{frame.tail(2)}')

# print(frame)
