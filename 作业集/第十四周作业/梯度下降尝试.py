import autograd.numpy as np
import pandas as pd
import scipy as sc
from autograd import grad
import matplotlib.pyplot as plt
from scipy import linalg
from sklearn.datasets import load_digits
from sklearn.datasets import fetch_california_housing
# 加载boston房价数据集
california = fetch_california_housing()
X = california.data
Y = california.target
#先进行PCA降维
X1=X.T#转置使得一列为一个数据   最后X1应该是64*1727大小
mean=X1.mean(axis=0)#对X1列向量进行中心化  先求出每一列的平均值
std=np.std(X1,axis=0)#求出每一列的标准差，接下来进行标准化处理
minimum=X1.min(axis=0)
maximum=X1.max(axis=0)
X1=(X1-minimum)/(maximum-minimum)#对X1数据进行minmax归一化处理
X2=X1.copy()
X2-=minimum
m=np.matmul(X2,X2.T)
eigenvalues, eigenvectors = linalg.eig(m)
D=8#原始数据维数为8
d=8#这里将数据降到d维
W=v=eigenvectors[:d]#这里W和v就是投影矩阵应该为d*D大小的矩阵
res=np.matmul(W,X1).T#np.matmul(W,X1)结果应为d*20640,每一列都是一个样本
Datas=pd.DataFrame(res,columns=[f"dim{i+1}" for i in range(d)])
Datas["label"]=Y
Datas=Datas.sample(frac=1).reset_index(drop=True)#将Datas数据集按照行进行打乱顺序
train_set=Datas.iloc[:20000]
test_set=Datas.iloc[20000:]#Datas一共有20640行数据，保留Datas的前20000行数据用于训练集，剩下的640行数据作为测试集
# #接下来使用梯度下降的方法进行拟合
#初始化w和b都是1
y_train=train_set["label"]
x_train=train_set.drop("label",axis=1).values.T#现在x_train就是一个d*1600大小的数据
# 定义成本函数，这里使用均方误差（MSE）
def cost(w, b, x_train, y_true):
    y_pred = np.matmul(w, x_train) + b
    return (np.mean((y_true - y_pred) ** 2))/2
# 计算损失函数关于w的偏导数
grad_w = grad(cost, 0)
# 计算损失函数关于b的偏导数
grad_b = grad(cost, 1)
w=np.ones((1,d),dtype=np.float32)#初始化w为全为1的向量
# w=np.array([[1,2,3,4,5,6,7,8]],dtype=np.float32)
b=0.0#初始化b的值为1.0
y=y_train.values
lr=0.001#初始化学习率为0.001
for epoch in range(2000):
    w_copy = w - lr * grad_w(w, b, x_train, y)
    b_copy = b - lr * grad_b(w, b, x_train, y)
    w=w_copy
    b=b_copy
    if epoch%100==0:
        print(f"现在是第{epoch}回合  目前成本函数值为：",cost(w,b,x_train,y))
n=30
x_test=test_set.iloc[:n,:-1].values.T#就取一条数据暂且（数据类型为series）
y_test=test_set.iloc[:n,-1].values
y_pre=np.matmul(w, x_test) + b
print("预测结果为：",np.round(y_pre.squeeze(),decimals=3))
print("真实结果为：",y_test)


