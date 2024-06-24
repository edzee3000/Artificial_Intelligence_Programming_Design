import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import linalg
from sklearn.datasets import load_digits
# 加载MNIST手写数据集
digits = load_digits()
X = digits.data
Y = digits.target
#先进行PCA降维
X1=X.T#转置使得一列为一个数据   最后X1应该是64*1727大小
mean=X1.mean(axis=0)#对X1列向量进行中心化  先求出每一列的平均值
std=np.std(X1,axis=0)#求出每一列的标准差，接下来进行标准化处理
minimum=X1.min(axis=0)
maximum=X1.max(axis=0)
X1=(X1-minimum)/(maximum-minimum)#对X1数据进行minmax归一化处理
m=np.matmul(X1,X1.T)
eigenvalues, eigenvectors = linalg.eig(m)
D=64#原始数据维数为64
d=32#这里将数据降到d维
W=v=eigenvectors[:d]#这里W和v就是投影矩阵应该为d*64大小的矩阵
res=np.matmul(W,X1).T#res结果应为d*1727,每一列都是一个样本
Datas=pd.DataFrame(res,columns=[f"dim{i+1}" for i in range(d)])
Datas["label"]=Y
Datas=Datas.sample(frac=1).reset_index(drop=True)#将Datas数据集按照行进行打乱顺序
train_set=Datas.iloc[:1600]
test_set=Datas.iloc[1600:]#Datas一共有1797行数据，保留Datas的前1600行数据用于训练集，剩下的197行数据作为测试集
#接下来进行KNN（k-nearest neighbors）
k=7
n=10
x_test=test_set.iloc[:n,:-1]#就取一条数据暂且（数据类型为series）
y_test=test_set.iloc[:n,-1].values
x_train=train_set.iloc[:,:-1]
y_train=train_set.iloc[:,-1]
predict=[]
for i in range(n):
    delta=x_test.iloc[i,:]-x_train
    delta["distance"]=((delta**2).sum(axis=1))**0.5
    delta["label"]=y_train
    delta=delta.sort_values(by="distance",ascending=True).reset_index(drop=True)
    print(delta)
    predict_i=delta.loc[:k,"label"].max()
    predict.append(predict_i)
predict=np.array(predict)
# predict=delta.iloc[:k,-1].max()
print("预测手写数字为：",predict)
print("真实手写数字为：",y_test)














