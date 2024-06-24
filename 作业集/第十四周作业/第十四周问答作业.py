

#
# #####电商数据预处理
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# ###数据清洗
# #加载OnlineRetail数据集
# Datas=pd.read_excel("Online Retail.xlsx")
# print("原数据为：",Datas)
# #去除包含缺失值的交易记录
# # Datas=Datas.dropna()
# Datas.dropna(inplace=True)
# Datas.reset_index(inplace=True)#更新Datas的索引
# print("去除包含缺失值的交易记录之后数据为：",Datas)
# #去除退货记录
# Datas=Datas[Datas["Quantity"]>=0]
# print("去除退货记录之后数据为：",Datas)
# ###数据集成
# # 计算每个用户的总购买金额
# group=Datas.groupby("CustomerID")
# # price_sum=group["UnitPrice"].sum()#这里一开始写错了忘了还有Quantity的存在
# new_data=Datas[["CustomerID"]].copy()
# new_data["mul_price"]=Datas["UnitPrice"]*Datas["Quantity"]
# price_sum=new_data.groupby("CustomerID").sum()
# print("每个用户的总购买金额为：\n",price_sum)
# # 计算每个用户的购买次数
# count=Datas["CustomerID"].value_counts()
# print("每个用户的购买次数为：\n",count)
# ###数据变换——将用户的总购买金额和购买次数进行标准化处理。
# #将用户的总购买金额归一化，这里统一使用z-score方法
# mean=price_sum["mul_price"].mean()
# std=price_sum["mul_price"].std()
# price_sum["standard_price"]=(price_sum["mul_price"]-mean)/std
# #将用户的购买次数归一化处理
# price_sum=pd.merge(price_sum,count,on="CustomerID")
# mean=price_sum["count"].mean()
# std=price_sum["count"].std()
# price_sum["standard_count"]=(price_sum["count"]-mean)/std
# print("经过归一化处理之后用户的总购买金额与购买次数为：\n",price_sum[["standard_price","standard_count"]])
#




#####使用PCA对词向量进行降维和可视化
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
# 加载预训练的GloVe词向量
def load_glove_embeddings(filepath):
   embeddings = {}
   with open(filepath, 'r', encoding='utf-8') as f:
       for line in f:
           values = line.split()
           word = values[0]
           vector = np.array(values[1:], dtype='float32')
           embeddings[word] = vector
   return embeddings
# glove_path = 'subset_glove.6B.50d.txt'
# embeddings = load_glove_embeddings(glove_path)
# # 选择一组词并提取其词向量
# words = ['king', 'queen', 'man', 'woman', 'apple', 'orange', 'france', 'germany', 'paris', 'berlin']
# # 初始化PCA并设置保留2个主成分
# pca=PCA(n_components=2)#表明要保留2维
# # 拟合数据
# embeddings=pd.DataFrame(embeddings.values(),index=embeddings.keys())
# print(embeddings)
# pca.fit(embeddings)
# # 转换数据
# pca_data = pca.transform(embeddings)
# pca_data=pd.DataFrame(pca_data,index=embeddings.index)
# print(pca_data)
# # 绘制散点图，x轴为0列，y轴为1列，索引(词名字)作为标签
# scatter=pca_data.plot.scatter(x=0, y=1, figsize=(8, 4.5),s=50,color="purple")
# # 将索引作为散点图的标签
# # scatter.set_xticks(pca_data[0].values)
# # scatter.set_xticklabels(pca_data.index.values)
# # scatter.set_yticks(pca_data[1].values)
# # scatter.set_yticklabels(pca_data.index.values)
# # 为每个点添加标签
# for i in range(len(pca_data)):
#     plt.annotate(pca_data.index[i], (pca_data.iloc[i,0], pca_data.iloc[i,1]),
#                  textcoords="offset points", xytext=(0,10), ha='center')
# plt.show()




# glove_path = ['subset_glove.6B.50d.txt','subset_glove.6B.100d.txt',
#              'subset_glove.6B.200d.txt','subset_glove.6B.300d.txt']
# embeddings = [load_glove_embeddings(i) for i in glove_path]
# # 选择一组词并提取其词向量
# words = ['king', 'queen', 'man', 'woman', 'apple', 'orange', 'france', 'germany', 'paris', 'berlin']
# figure=plt.figure(figsize=(10, 6))
# for i in range(len(embeddings)):
#     data=embeddings[i]
#     # 初始化PCA并设置保留2个主成分
#     pca=PCA(n_components=2)#表明要保留2维
#     # 拟合数据
#     data=pd.DataFrame(data.values(),index=data.keys())
#     print(data)
#     pca.fit(data)
#     # 转换数据
#     pca_data = pca.transform(data)
#     pca_data=pd.DataFrame(pca_data,index=data.index)
#     # print(pca_data)
#     # 绘制散点图，x轴为0列，y轴为1列，索引(词名字)作为标签
#     pca_data.plot.scatter(x=0, y=1, ax=plt.subplot(2, 2, i) , s=50 , color="purple")
#     # 为每个点添加标签
#     for j in range(len(pca_data)):
#         plt.annotate(pca_data.index[j], (pca_data.iloc[j,0], pca_data.iloc[j,1]),
#                      textcoords="offset points", xytext=(0,10), ha='center')
# plt.plot()
































