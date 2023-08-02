import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



randn = np.random.randn(100)
sns.kdeplot(data=randn)
sns.rugplot(data=randn)
plt.show()

# print(randn)
