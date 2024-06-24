import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import linalg
from sklearn.datasets import load_digits
# 加载MNIST手写数据集
digits = load_digits()
X = digits.data
Y = digits.target
# 进行PCA降维
# Y=Y.reshape(1,-1)
# print("X数据为：",X)
# print("Y数据为：",Y)
# print("X种类为：",type(X))
# print("Y种类为：",type(Y))
X1=X.T#转置使得一列为一个数据   最后X1应该是64*1727大小
mean=X1.mean(axis=0)#对X1列向量进行中心化  先求出每一列的平均值
std=np.std(X1,axis=0)#求出每一列的标准差，接下来进行标准化处理
minimum=X1.min(axis=0)
maximum=X1.max(axis=0)
# X1=(X1-mean)/std #对X1数据进行中心化处理与z-score标准化处理
X1=(X1-minimum)/(maximum-minimum)#对X1数据进行minmax归一化处理
m=np.matmul(X1,X1.T)
eigenvalues, eigenvectors = linalg.eig(m)
D=64#原始数据维数为64
d=32#这里将数据降到d维
# print(eigenvalues)#eigenvalues都是经过从大到小排序过后的
# print(eigenvectors)
W=v=eigenvectors[:d]#这里W和v就是投影矩阵应该为d*64大小的矩阵
res=np.matmul(W,X1).T#res结果应为d*1727,每一列都是一个样本
# print(res)
#可视化
Datas=pd.DataFrame(res,columns=[f"dim{i+1}" for i in range(d)])
Datas["label"]=Y
print(Datas)
# figure=plt.figure(figsize=(10,8))
# subdata=Datas.loc[Datas["label"]==4 | Datas["label"]==6]
subdata = Datas[(Datas['label'] == 3) | (Datas['label'] == 4)]#单独只看数字3和数字4
Datas.plot.scatter(x="dim1",y="dim2",c=Y,cmap='viridis')# 使用颜色映射cmap
plt.title("将全体数据经过PCA之后取出维数为1和2的平面")
plt.xlabel("dim1")
plt.ylabel("dim2")
subdata.plot.scatter(x="dim12",y="dim13",c=subdata["label"],cmap='viridis')# 使用颜色映射cmap
plt.title("取出数字3和数字4的数据，且PCA之后维数为12和13的平面")
plt.xlabel("dim12")
plt.ylabel("dim13")


# 设置字体为SimHei，确保支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# 或者使用matplotlib内置的字体名称
# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 设置正常显示中文
plt.rcParams['axes.unicode_minus'] = False
plt.show()
