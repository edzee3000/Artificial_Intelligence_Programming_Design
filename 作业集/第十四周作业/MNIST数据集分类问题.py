




######使用分类模型对手写数字数据集进行分类（KNN模型）
import numpy as np
from sklearn.datasets import load_digits
from sklearn.neighbors import KNeighborsClassifier#这里使用K近邻KNN算法
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score#这里用于报告评估模型的结果以及准确率
# 加载数据
digits = load_digits()
X = digits.data
Y = digits.target
# 分割数据集
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)#test_size表示测试集数据占20%，random_state设置随机数生成器的种子保证每一次结果可以复现
# 创建KNN模型的实例
KNN = KNeighborsClassifier(n_neighbors=9)
# 训练模型
KNN.fit(X_train, Y_train)
# 预测
Y_pred = KNN.predict(X_test)
# 评估模型
print(classification_report(Y_test, Y_pred))
print(accuracy_score(Y_test, Y_pred))
#接下来使用训练好的模型进行预测
import random
x_data=X[88:100]
y_data=Y[88:100]
x_data=scaler.fit_transform(x_data)#使用StandardScalar.fit_transform()函数进行标准化处理
y_predict=KNN.predict(x_data)
print("预测结果手写数字为：",y_predict)
print("真实结果手写数字为：",y_data)
























######使用分类模型对手写数字数据集进行分类（神经网络）
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import load_digits#导入MNIST手写数字数据集
from torch.utils.data import DataLoader, Dataset
#定义聚合数据集的类CustomDataset
class CustomDataset(Dataset):
    def __init__(self,datas,labels):
        # 假设有一些自定义的数据
        self.data = torch.tensor(datas, dtype=torch.float32)
        self.targets = torch.tensor(labels, dtype=torch.long)
        self.mean = self.data.mean()
        self.std = self.data.std()
    def __len__(self):
        return len(self.targets)
    def __getitem__(self, index):
        # x = self.data[index]
        # y = self.targets[index]
        x = (self.data[index] - self.mean) / self.std
        y = self.targets[index]
        return x, y
# 定义神经网络类
class NetWork(nn.Module):
    def __init__(self):
        super(NetWork, self).__init__()
        self.fc1 = nn.Linear(64, 120)
        self.fc2 = nn.Linear(120, 40)
        self.fc3 = nn.Linear(40, 20)
        self.fc4 = nn.Linear(20, 10)
        self.logsoftmax = nn.LogSoftmax(dim=1)  # 使用LogSoftmax激活函数最后选出概率最大的那个类别
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        x = torch.relu(self.fc4(x))
        x = self.logsoftmax(x)  # 使用LogSoftmax
        return x
# 加载数据
digits = load_digits()
X = digits.data
Y = digits.target
# 实例化自定义数据集
dataset = CustomDataset(X,Y)
# 创建数据加载器
dataloader = DataLoader(dataset=dataset, batch_size=64, shuffle=True)
net = NetWork()
# 损失函数和优化器
criterion = nn.CrossEntropyLoss()  # 使用CrossEntropyLoss交叉损失函数
optimizer = optim.Adam(net.parameters(), lr=0.001)# 使用Adam优化器
# optimizer = optim.SGD(net.parameters(), lr=0.0001, momentum=0.9)# 使用SGD优化器
# 训练网络
for epoch in range(30):
    for inputs, labels in dataloader:
        optimizer.zero_grad()# 清零梯度
        outputs = net(inputs)# 前向传播
        # labels = labels.unsqueeze(1)  # 将 labels 视为列向量
        loss = criterion(outputs, labels)# 计算损失
        loss.backward()# 反向传播
        optimizer.step()# 更新权重
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
        # print("标签为：",labels)
        # print("预测为：",predicted)
        correct += (predicted == labels).sum().item()
    print(f'Accuracy of the network: {100 * correct / total}%')