
# print(sum(range(5),-1))
# from numpy import *
# import numpy as np
# print(np.sum(range(5),-1))

# import numpy as np
# arr=np.random.rand(6,10)
# arr.sort()


import seaborn as sns
import pandas as pd
a = pd.read_csv("E:/数据集合集/seaborn-data/anscombe.csv")
print(a.info())
print(a.describe())
print("DataFrame的数据个数为：",a.count())

