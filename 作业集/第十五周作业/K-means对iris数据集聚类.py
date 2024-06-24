#K-means算法对鸢尾花（Iris）数据集进行聚类，并评估聚类结果的质量
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
# 读取数据集
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = pd.read_csv(url, header=None)#iris数据集大小为150*5
data.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']#class这一列一共有3种类别
#数据预处理（选择前4列进行数据预处理，最后一列其实是类别）
X=data.iloc[:,:-1]
min_num=X.min(axis=0)
max_num=X.max(axis=0)
data.iloc[:,:-1]=(X-min_num)/(max_num-min_num)#对前4列进行minmax标准化处理
category=data["class"].unique()#将鸢尾花的种类进行one-hot编码处理
for i in category:
    data[i]=(data["class"]==i).astype(int)/5
data.drop("class",axis=1,inplace=TrSue)#经过数据预处理之后，data数据集大小变为150*7
#接下来使用K-means算法进行聚类（使用全部150条数据）
data["kind"]=0#初始化所有的点都是同一簇的设置其类别为0
K=3#首先先设定K值为3类
data = data.sample(frac=1).reset_index(drop=True)#然后选取初始簇中心，先打乱data顺序，然后取前k行
data.iloc[:K,-1]=range(K)#将前K行数据分别作为类别0,1,……,K
def cal_dist(center,data):
    '''用于计算每个点到簇中心的距离
    注意这里的center就是簇中心应该是DataFrame格式注意是有种类的，data是数据集150*8大小DataFrame'''
    dist=[]
    data=data.copy()
    for i in range(K):
        cluster_center=center.iloc[i]
        X=data.iloc[:,:-1].values
        cluster_center=cluster_center.values
        Distance=np.mean((X-cluster_center[:-1])**2,axis=1)**0.5
        dist.append(Distance)
    dist=np.array(dist).T
    type=np.argmin(dist,axis=1)
    data["kind"]=type
    return data
def cal_center(data):
    '''计算已知cluster的150*8给定data数据集的每一簇的中心点'''
    gr=data.groupby("kind")
    center=gr.agg("mean").reset_index(drop=True)
    center["kind"]=center.index
    return center
center=data.iloc[:K]
data_copy=cal_dist(center,data)
while not data_copy["kind"].equals(data["kind"]):
    data = data_copy
    center = cal_center(data)
    data_copy = cal_dist(center, data)
data = data_copy
print("最后聚类结果为：",data)
#接下来进行可视化操作（就取前三列可视化好了）
# 创建一个3D图形对象
figure = plt.figure()
# 将3D图形对象添加到坐标轴
ax = figure.add_subplot(111, projection='3d')
# 使用scatter方法绘制3D散点图
# colors={0:"red",1:"black",3:"blue"}
colors = data["kind"]  # 生成与数据点对应的颜色值
pca=PCA(n_components=3)#表明要保留2维
pca.fit(data)
pca_data = pca.transform(data)
pca_data=pd.DataFrame(pca_data,index=data.index)
ax.scatter(pca_data.iloc[:,0],pca_data.iloc[:,1],pca_data.iloc[:,2],c=colors,cmap='viridis')
# 设置坐标轴标签
# ax.set_xlabel(data.columns[0])
# ax.set_ylabel(data.columns[1])
# ax.set_zlabel(data.columns[2])
ax.set_xlabel("dim1")
ax.set_ylabel("dim2")
ax.set_zlabel("dim3")
# 显示图像
plt.show()


