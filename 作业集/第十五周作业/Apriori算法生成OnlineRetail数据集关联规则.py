import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# path="Online Retail.xlsx"
# datas=pd.read_excel(path)
# # 保存为CSV文件
# datas.to_csv('Online Retail.csv', index=False)#因为用excel表格打开太慢了，先转化为csv文件，之后读取的话会快很多
#读取数据
path="Online Retail.csv"
datas=pd.read_csv(path)
#对数据进行预处理
datas.dropna().reset_index(drop=True,inplace=True)#对nan数据去除（测试之后发现竟然没有缺失值）
X=datas.iloc[:,[2,3,-1]]#取出X表示待分析关联规则的数据（已知前2列数据是ID不是特征），一共有541909*3个数据
X=X[X["Quantity"]>0]#只保留数量>0的部分
elements = []#存储待分析的元素
l=X.shape[0]#存储X有多少行数据
S=0.01#设置支持度为0.00001
C=0.5#设置置信度为0.5
for column in X.columns:
    # a=X[column].unique().tolist()#a表示每一列有的元素
    # elements+=a
    b=X[column].value_counts()
    for i in range(len(b)):
        if b.iloc[i]/l>S:
            elements.append(b.index[i])
# new_elements=[for i in range(len(elements)) for j in range(i,j)]
black_list=[]
def search(have_elements,pre_elements,new_ele):
    '''have_elements表示已经有的元素,pre_elements表示等待被放进去的元素'''
    have_elements=have_elements.copy()
    print(have_elements)
    if len(pre_elements)==0:
        new_ele.append(have_elements)
        return new_ele
        # return set(have_elements)
    for i in pre_elements:
        new_have=have_elements.copy()
        new_have.append(i)
        print(new_have)
        if set(have_elements) in black_list or set(have_elements) in new_ele:
            continue
        else:
            new_ele.append(new_have)
            pre_ele_new=[j for j in pre_elements if j!=i]
            if cal_frequency(new_have,datas)>S:
                search(new_have,pre_ele_new,new_ele)
            else:
                black_list.append(set(have_elements))
    return new_ele
def cal_frequency(ele,datas):
    fre = datas.apply(lambda x: set(ele).issubset(x), axis=1).astype(int).sum()
    print("fre为：",fre)
    return fre/l

print(elements)
a=search([],elements,[])
print(a)
