import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
# 加载数据集
california = fetch_california_housing()
X, y = california.data, california.target
# 数据标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
# 应用PCA降维
pca = PCA(n_components=8)  # 降维到8个特征
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)
# 定义模型参数
def model(X, w, b):
    return np.dot(X, w) + b
# 定义损失函数（均方误差）
def loss(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)
# 定义梯度计算
def gradients(w, b, X, y):
    y_pred = model(X, w, b)
    grad_w = -2 * np.dot(X.T, (y - y_pred)) / len(y)
    grad_b = -2 * np.sum(y - y_pred) / len(y)
    return grad_w, grad_b
# 初始化参数
w = np.zeros(pca.n_components_)
b = 0
learning_rate = 0.01
epochs = 1000
# 梯度下降训练过程
for epoch in range(epochs):
    grad_w, grad_b = gradients(w, b, X_train_pca, y_train)
    w -= learning_rate * grad_w
    b -= learning_rate * grad_b
    if epoch % 100 == 0:
        loss_value = loss(y_train, model(X_train_pca, w, b))
        print(f"Epoch {epoch}: Loss: {loss_value}")
# 在测试集上进行预测
y_pred = model(X_test_pca, w, b)
# 评估模型性能
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error on Test Set: {mse}")

x=X_test[:10]
y=y_test[:10]
print(model(x,w,b))
print(y)
