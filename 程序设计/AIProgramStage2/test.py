import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
import numpy as np
import os,glob
import csv
import random
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import Dataset
import torch.optim as optim
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(260, 120)
        self.fc2 = nn.Linear(120, 40)
        self.fc3 = nn.Linear(40, 20)
        self.fc4 = nn.Linear(20, 10)
        self.fc5 = nn.Linear(10, 1)
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        x = torch.relu(self.fc4(x))
        x = self.fc5(x)
        return x
# 加载模型参数
model = SimpleNet()  # 假设 SimpleNet 是你的模型类
model.load_state_dict(torch.load('net.pth'))
# 如果你保存了整个模型
# model = torch.load('complete_model.pth')



file= "掼蛋数据集1.0"
Datas=pd.read_csv(file)
Datas=Datas.iloc[:,1:]
print(Datas.columns.values)
print(Datas)
#数据预处理
new_Datas=pd.DataFrame(columns=["出牌","我方牌序列","对方牌序列","回合数","胜负","Q值"])
x_datas=[]
y_datas=[]
for i in range(len(Datas)):
    data=[]
    x_data=[]
    a1=Datas.iloc[i,1]
    if a1=="不出":
        x_data+=[0]*6
        data.append(np.array([0]*6))
    else:
        a1=a1[1:len(a1)-1].split()
        a1=list(map(int,a1))
        a1+=[0]*(6-len(a1))
        x_data+=a1
        a1=np.array(a1)
        data.append(a1)
    a2=Datas.iloc[i,2]
    a2 = a2[1:len(a2) - 1].split()
    a2 = list(map(int, a2))
    a2+=[0]*(27-len(a2))
    x_data+=a2
    a2 = np.array(a2)
    data.append(a2)
    a3 = Datas.iloc[i, 3]
    a3 = a3[1:len(a3) - 1].split()
    a3 = list(map(int, a3))
    a3 += [0] * (27 - len(a3))
    x_data+=a3
    a3 = np.array(a3)
    data.append(a3)
    a4=int(Datas.iloc[i,4])
    data.append(a4)
    a5 = int(Datas.iloc[i, 5])
    data.append(a5)
    a6 = int(Datas.iloc[i, 6])
    data.append(a6)
    new_Datas.loc[len(new_Datas)] = data
    x_data+=[a4]*100
    x_data+=[a5]*100
    x_datas.append(x_data)
    y_datas.append(a6)
print(new_Datas)

x_test=torch.tensor(x_datas,dtype=torch.float32)




# 将模型设置为评估模式
model.eval()

# 确保在测试或推理时不计算梯度
with torch.no_grad():
    # 使用加载的模型进行预测
    predictions = model(x_test)
    print(predictions)







