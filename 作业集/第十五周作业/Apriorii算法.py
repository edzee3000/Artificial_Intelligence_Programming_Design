import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#读取数据
path="Online Retail.csv"
datas=pd.read_csv(path)
#对数据进行预处理
datas.dropna().reset_index(drop=True,inplace=True)#对nan数据去除（测试之后发现竟然没有缺失值）
X=datas.iloc[:,[2,3,-1]]#取出X表示待分析关联规则的数据（已知前2列数据是ID不是特征），一共有541909*3个数据
elements = []#存储待分析的元素
l=X.shape[0]#存储X有多少行数据
S=0.05#设置支持度为0.01
C=0.5#设置置信度为0.5
def cal_frequency(ele,datas):#计算组合出现的频率
    fre = datas.apply(lambda x: set(ele).issubset(x), axis=1).astype(int).sum()
    print("频率为：",fre/l)
    return fre/l
for column in X.columns:#计算所有可能元素
    b=X[column].value_counts()
    for i in range(len(b)):
        if b.iloc[i]/l>S:
            elements.append(b.index[i])
print(elements)#elements其实就是所有元素
#接下来先求所有的频繁项集
open_list=[{i} for i in elements]
close_list=[]#表示已经遍历过的元素
res=[[i] for i in elements]
frequencies=[cal_frequency(i,datas) for i in open_list]
print(frequencies)
def width_search(not_have):#广度优先搜索
    not_have_copy=not_have.copy()
    global open_list
    while len(open_list)!=0:
        open=[]
        for i in open_list:#i表示现在的有的元素   比如[1,2,3,4,5]现在有了[{1}{2}{3}{4}{5}]
            not_have_list=[j for j in not_have_copy if j not in i]
            for j in not_have_list:
                print(not_have_list)
                print(i)
                new=i.copy()
                new.add(j)
                print("new为：", new)
                frequent=cal_frequency(list(new),datas)
                if new not in close_list and frequent>S:
                    open.append(new)
                    res.append(list(new))
                    frequencies.append(frequent)
                close_list.append(new)
        open_list=open
width_search(elements)
itemset=pd.DataFrame({"频繁项集":res,"频率":frequencies})
print("频繁项集为：",itemset)
#接下来生成关联规则
open_list=[]
close_list=[]#表示已经遍历过的元素
res=pd.DataFrame([],columns=["前件","后件"])
def cal_convince(consequence,s):
    '''计算consequence的置信度'''
    global itemset
    index_iloc1 = itemset.iloc[itemset['频繁项集'].values == list(consequence[0])].index
    probility1=itemset['频繁项集'][index_iloc1]
    index_iloc2 = itemset.iloc[itemset['频繁项集'].values == list(s)].index
    probility2 = itemset['频繁项集'][index_iloc2]
    return probility2/probility1
def split_list(itemset):#仍然使用广度优先
    '''将一个itemset拆分为n->m的形式'''
    global open_list,res,close_list
    open_list=[set([i]) for i in itemset]
    for i in open_list:
        remain = [j for j in itemset if j not in i]
        consequence=[set(remain),i]
        if consequence not in close_list and cal_convince(consequnce,itemset)>C:
            res.iloc[len(res)] = list(new)
        close_list.append(consequnce)
    while len(open_list)!=0:
        open = []
        for i in open_list:
            remain=[j for j in itemset if j not in i]
            for j in remain:
                new = i.copy()
                new.add(j)
                remain=[k for k in remain if k!=j]
                consequnce=[set(remain),new]
                if consequnce not in close_list and cal_convince(consequnce,remain+list(new))>C:#这里直接计算置信度
                    open.append(consequnce)
                    res.iloc[len(res)]=list(new)
                close_list.append(consequnce)
        open_list = open
for i in range(len(itemset["频繁项集"])):
    if len(itemset["频繁项集"][i])<2:
        continue
    split_list(itemset["频繁项集"][i])


