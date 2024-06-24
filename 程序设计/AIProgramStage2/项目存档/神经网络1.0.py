


import numpy as np
import os,glob
import csv
import random
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import Dataset
import torch.optim as optim
# from torchvision import transforms
# from PIL import Image
from torch.utils.data import DataLoader
import cv2
# from einops.layers.torch import Reaarange


class Network(torch.nn.Module):
    def __init__(self,n_features,n_hidden,n_output):#初始化函数
        super(Network,self).__init__()#调用父类的初始化
        self.hidden=torch.nn.Linear(n_features,n_hidden)#自定义hidden隐藏层
        self.predict=torch.nn.Linear(n_hidden,n_output)#由于这里只是简单地撘一个神经网络就只设置一个隐藏层就好
    def forward(self,x):#前向传播函数
        x=F.relu(self.hidden(x))
        x=self.predict(x)
        return x






# 一个示例状态
state = [1, 14, 2, 3, 1, 10]  # 假设手牌是红桃A和黑桃3，公共牌是红桃10
# 将状态转换为PyTorch张量
state_tensor = torch.tensor(state, dtype=torch.float32).unsqueeze(0)  # 添加batch维度
# 定义神经网络
class PokerNet(nn.Module):
    def __init__(self):
        super(PokerNet, self).__init__()
        self.fc1 = nn.Linear(6, 128)  # 输入层，6个输入（3张牌，每张牌用两个数字表示）
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 1)  # 输出层，输出一个Q值
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x
# 创建神经网络实例
net = PokerNet()






# 定义DQN网络结构
class DQN(nn.Module):
    def __init__(self, input_size=60, hidden_size1=120, hidden_size2=40,hidden_size3=20, output_size=1):
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size1)
        self.fc2 = nn.Linear(hidden_size1, hidden_size2)
        self.fc3 = nn.Linear(hidden_size2, hidden_size3)
        self.fc4 = nn.Linear(hidden_size3, output_size)
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        x = self.fc4(x)
        return x
# 定义DQN Agent
class DQNAgent:
    def __init__(self,learning_rate, gamma):
        self.policy_net = DQN()
        self.target_net = DQN()
        self.target_net.load_state_dict(self.policy_net.state_dict())
        self.target_net.eval()
        self.optimizer = optim.Adam(self.policy_net.parameters(), lr=learning_rate)
        self.gamma = gamma
    def select_action(self, state, epsilon):
        if torch.rand(1) < epsilon:
            return torch.randint(0, self.policy_net.fc2.out_features, (1,))
        else:
            with torch.no_grad():
                return torch.argmax(self.policy_net(state))
    def train(self, batch):
        states, actions, rewards, next_states, dones = batch
        # 计算Q值
        Q_values = self.policy_net(states).gather(1, actions)
        # 计算目标Q值
        next_Q_values = self.target_net(next_states).max(1)[0].unsqueeze(1)
        target_Q_values = rewards + (1 - dones) * self.gamma * next_Q_values
        # 计算损失
        loss = nn.functional.smooth_l1_loss(Q_values, target_Q_values)
        # 优化模型
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
    def update_target_network(self):
        self.target_net.load_state_dict(self.policy_net.state_dict())
















import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
# 创建自定义数据集
class CustomDataset(Dataset):
    def __init__(self,datas,labels):
        # 假设有一些自定义的数据
        self.data = torch.tensor(datas, dtype=torch.float32)
        self.targets = torch.tensor(labels, dtype=torch.float32)
    def __len__(self):
        return len(self.targets)
    def __getitem__(self, index):
        x = self.data[index]
        y = self.targets[index]
        return x, y
# 定义神经网络
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

#读取数据集并且对数据进行预处理
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
# 创建DQNAgent实例
agent = DQNAgent(learning_rate=1e-3, gamma=0.99)
# 示例训练代码
# for episode in range(num_episodes):
#     state = env.reset()
#     done = False
#     total_reward = 0
#     while not done:
#         action = agent.select_action(torch.tensor(state).float().unsqueeze(0), epsilon)
#         next_state, reward, done, _ = env.step(action.item())
#         total_reward += reward
#         # 存储经验
#         memory.push(state, action, next_state, reward, done)
#         # 更新状态
#         state = next_state
#         # 如果记忆足够，开始训练
#         if len(memory) > batch_size:
#             batch = memory.sample(batch_size)
#             agent.train(batch)
#     # 更新目标网络
#     if episode % target_update_freq == 0:
#         agent.update_target_network()
#     print(f"Episode {episode}, Total Reward: {total_reward}")

# 实例化自定义数据集
dataset = CustomDataset(x_datas,y_datas)
# 创建数据加载器
dataloader = DataLoader(dataset=dataset, batch_size=5, shuffle=True)
net = SimpleNet()
# 损失函数和优化器
# criterion = nn.CrossEntropyLoss()
criterion = nn.MSELoss()  # 均方误差损失，常用于回归任务
# optimizer = optim.Adam(model.parameters(), lr=learning_rate)
optimizer = optim.Adam(net.parameters(), lr=0.1)
# 训练网络
for epoch in range(10):
    for inputs, labels in dataloader:
        # 清零梯度
        optimizer.zero_grad()
        # 前向传播
        outputs = net(inputs)
        # 计算损失
        loss = criterion(outputs, labels)
        # 反向传播
        loss.backward()
        # 更新权重
        optimizer.step()
    print(f'Epoch {epoch+1}, Loss: {loss.item()}')
# 测试网络
net.eval()
with torch.no_grad():
    correct = 0
    total = 0
    for inputs, labels in dataloader:
        outputs = net(inputs)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
    print(f'Accuracy of the network: {100 * correct / total}%')


torch.save(net.state_dict(), 'net.pth')  # 保存模型参数

