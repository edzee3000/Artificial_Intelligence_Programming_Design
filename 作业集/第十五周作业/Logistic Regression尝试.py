import autograd.numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import linalg
from autograd import grad

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
    return Datas.iloc[:14,:-1].values,\
            Datas.iloc[:14,-1].values,\
            Datas.iloc[14:,:-1].values,\
            Datas.iloc[14:,-1].values
def p1(x,beta):
    '''预测y为1的函数'''
    column_sum = (beta * x).sum(axis=1)  # 结果是一个1维向量
    exp_res=np.exp(column_sum)
    return exp_res/(1+exp_res)
def p0(x,beta):
    '''预测y为0的函数'''
    column_sum = (beta * x).sum(axis=1)  # 结果是一个1维向量
    exp_res = np.exp(column_sum)
    return 1/(1+exp_res)
#首先先读取boston_house_prices数据
path="xigua_data3.0.csv"
Datas=pd.read_csv(path)
#对数据进行预处理
mapping={"浅白":0.0,"青绿":0.5,"乌黑":1.0,
         "硬挺":0.0,"稍蜷":0.5,"蜷缩":1.0,
         "清脆":0.0,"沉闷":0.5,"浊响":1.0,
         "模糊":0.0,"稍糊":0.5,"清晰":1.0,
         "平坦":0.0,"稍凹":0.5,"凹陷":1.0,
         "软粘":0.0,"硬滑":1.0,
         "否":0,"是":1}
# 应用映射到DataFrame
for column in Datas.columns:
    if Datas[column].dtype == object:  # 只处理对象类型（字符串）的列
        Datas[column] = Datas[column].replace(mapping)
Datas.drop("编号",axis=1,inplace=True)#Datas去除编号之后一共有17*9个数据，8个特征，1个label
#接下来不妨取14行数据作为训练集，3行数据用于测试集，注意此处就不进行PCA降维了，直接标准化处理maxmin即可
Datas,min_num,max_num=process_datas(Datas)
Datas = Datas.sample(frac=1).reset_index(drop=True)
x_train,y_train,x_test,y_test=split_datas(Datas)
x_train=np.append(x_train,np.ones((len(x_train),1)),axis=1)
x_test=np.append(x_test,np.ones((len(x_test),1)),axis=1)
y_train,y_test=y_train.reshape(1,-1),y_test.reshape(1,-1)
beta=np.zeros((1,9),dtype=np.float32)#初始化beta（w和b拼接一下有9维）全为1
#接下来计算l(beta)损失函数
def l(beta,x,y):
    column_sum=(beta*x).sum(axis=1)#结果是一个1维向量
    res1=-y*column_sum
    res2=np.log(1+np.exp(column_sum))
    return (res1+res2).sum()
# 计算损失函数l关于beta的偏导数
grad_beta = grad(l, 0)
lr=0.01#初始化学习率为0.001
for epoch in range(2000):
    beta -= lr * grad_beta(beta,x_train,y_train)
    if epoch%100==0:
        print(f"现在是第{epoch}回合  目前成本函数值为：",l(beta,x_train,y_train))
print("训练误差为：",l(beta,x_train,y_train))
#接下来用测试集去测试
probility_yes=p1(x_test,beta)
print("预测概率为：",probility_yes)
probility_yes=np.where(probility_yes>0.5,1,0)
print("预测结果为：",probility_yes)
print("实际结果为：",y_test.reshape(-1,))
print("泛化误差为：",l(beta,x_test,y_test))
print("beta参数为：",beta)
