import random

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({'month': [1, 4, 7, 10],
'year': [2012, 2014, 2013, 2014],
'sale':[55, 40, 84, 31]})

mul_data = df.set_index(['year','month'])
print(mul_data.index)


arr_index = [[1,1,2],['r','g','b']]
mul_index_data = pd.MultiIndex.from_arrays(arr_index, names=('深度','颜色' ))
print(mul_index_data)
to_set_index = np.random.randn(3, 5)
frame = pd.DataFrame(to_set_index, index=mul_index_data)
print(frame)
