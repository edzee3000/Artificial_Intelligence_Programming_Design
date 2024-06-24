# import pandas as pd
# # 假设您有一个DataFrame df
# df = pd.read_csv('boston_house_prices.csv')
# # 定义一个列表，包含您想要检查的元素
# elements_to_check = ["0.00632", "18" ,"2.31"]
#
# # 创建一个Series，其中包含列表中的元素
# check_series = pd.Series(elements_to_check)
#
# # 使用str.contains()方法检查每一行是否包含列表中的元素
# contains_series = df.applymap(lambda x: check_series.str.contains(x, na=False),axis=1)
#
# # 计算每个元素在每一行中出现的频率
# frequency_series = contains_series.sum()
#
# # 打印频率
# print(frequency_series)



# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# A=np.array([[0.39,-1.89],
#             [0.61,-1.80],
#             [0.93,-1.68],
#             [1.35,-1.50]],dtype=np.float32)
# B=np.ones((4,1))
# X=np.matmul(np.matmul(np.linalg.inv(np.matmul(A.T,A)),A.T),B)
# print(X)

# def function_set(A,X,B):
#     '''注意这里面X和B最好都是列向量'''
#     return np.matmul(A,X)-B
# def f(a,x,y,b):
#     '''隐函数形式'''
#     # return (a*np.array((x,y)).reshape(2,400).T).sum()-b
#     return a[0]*x+b[0]*y-b
# def f1(a,x,b):
#     return -a[0]/a[1]*x+b/a[1]
# 生成 x 值，范围从 -2*pi 到 2*pi
# X = np.linspace(-0.0000000000001,0.0000000000001, 400).reshape(1,-1)
# Y = np.linspace(0.9999999999999,1.0000000000001, 400).reshape(1,-1)
# X, Y = np.meshgrid(X, Y)
# X = np.linspace(-10,10, 400)
# Y = np.linspace(-10,10, 400)
# print(X)
# print(Y)
# 计算 f(x)
# res = function_set(A,(np.vstack((X,Y))),B)
# print(res)
# 找出满足 f(x, y) = 0 的点
# print(X)
# plt.figure(figsize=(8, 8))
# for i in range(len(A)):
#     # plt.contour(X, Y, f(A[i],X, Y,B[i]), levels=[0], colors='red')
#     plt.plot(X, f1(A[i],X,B[i]), label=f"{i}",color="red")
# plt.show()
# a=set({1})
# new=a.copy()
# new.add(2)
# print(new)
#
# df=pd.DataFrame([[1,2],[4,3]],columns=["dim1","dim2"])
# print(df["dim1"][1])
# res=pd.DataFrame([],columns=["前件","后件"])
# print(res)





# x=(1,2)
# y=(1,2)
# print(y is x)
# print(y==x,"\n")
# x=[1,2]
# y=[1,2]
# print(y is x)
# print(y==x,"\n")
# x,y=tuple(x),tuple(y)
# print(y is x)
# print(y==x,"\n")

# from copy import deepcopy
# x=(3,2,1,5)
# y=deepcopy(x)
# print(y)
# x=sorted(x)
# print(x)
# x=[3,2,1,4]
# x.sort()
# print(x)
# x=[(1,2,3),2,3,4]
# y=deepcopy(x)
# print(y[0] is x[0])
# x=([1,2,3],2,3,4)
# y=deepcopy(x)
# print(y[0] is x[0])








import numpy as np
# x=np.arange(5)
# y=[True, True, False, True, False]
# z=np.add(x,5,where=y)
# print(x)
# print(y)
# print(z)
# print("\n")
#
# x= np.arange(5)
# y=x%3==0
# z=np.add(x,5,where =y)
# print(x)
# print(y)
# print(z)


# x = np.random.rand(10)
# print(x)
# print(x > 0.2)
# print((-0.2 < x) * ( x < 0.2))
# print((-0.2 < x) & ( x < 0.2))

list1=[1,2,3]
def f(x):
    x[0]=2
    return x
print(id(list1))
f(list1)
print(id(list1))
