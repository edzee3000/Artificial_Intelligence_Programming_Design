import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import linalg
#首先先读取boston_house_prices数据
path="boston_house_prices.csv"
Datas=pd.read_csv(path)
#然后对数据进行预处理
def process_datas(Datas):
    '''注意这里传进来的应该是整个Datas，只需要对X进行标准化处理minmax，并且需要返回Datas
    之后对于新的数据就写一个新的函数去进行数据处理'''
    #通过视图先对Datas的X进行标准化minmax处理
    X=Datas.iloc[:,:-1]
    min_num=X.min(axis=0)
    max_num=X.max(axis=0)
    Datas.iloc[:,:-1]=(X-min_num)/(max_num-min_num)
    return Datas,min_num,max_num
def split_datas(Datas):
    '''由于这里已知Datas为506*13的数据集，因此直接返回即可
    返回顺序为x_train,y_train,x_test,y_test'''
    return Datas.iloc[:500,:-1].values,\
            Datas.iloc[:500,-1].values,\
            Datas.iloc[500:,:-1].values,\
            Datas.iloc[500:,-1].values
Datas.drop("B",axis=1,inplace=True)#需要先删除带有种族歧视的那一列
#Datas是一个506*13的数据不妨让前500个数据是训练集，后6个数据是测试集  12个特征，1个label
#这里不妨先不进行PCA降维（反正维数也不算高），直接进行数据的标准化处理好了
Datas,min_num,max_num=process_datas(Datas)
Datas = Datas.sample(frac=1).reset_index(drop=True)
x_train,y_train,x_test,y_test=split_datas(Datas)
x_train=np.append(x_train,np.ones((len(x_train),1)),axis=1)
x_test=np.append(x_test,np.ones((len(x_test),1)),axis=1)
y_train,y_test=y_train.reshape(1,-1),y_test.reshape(1,-1)
# print(x_train,y_train,x_test,y_test)
#接下来求多元线性回归w_hat的闭式解，根据公式 w* = (X^T * X)^−1 * X^T * y
w_hat=np.matmul(np.matmul(linalg.inv(np.matmul(x_train.T,x_train)) , x_train.T)
                , y_train.T).T
#接下来求出训练误差与泛化误差
def f(x):
    '''注意传进来的是x，不需要w_hat，这里的w_hat需要在global frame当中
    这里的x可以是一个矩阵哦，相信numpy广播的力量，就不用自己再for循环了hhh'''
    global w_hat
    return (w_hat*x).sum(axis=1)
def MSE(y_pre,y_true):
    return np.mean((y_pre-y_true)**2)**0.5
Train_Result=f(x_train)
Train_Error=MSE(Train_Result,y_train)
print("训练误差为：",Train_Error)
Test_Result=f(x_test)
Test_Error=MSE(Test_Result,y_test)
print("泛化误差为：",Test_Error)
print("测试集上数据预测结果为：",Test_Result)
print("测试集上数据真实值为：",y_test)
