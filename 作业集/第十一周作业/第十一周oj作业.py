'''
#接收输入
import numpy as np
arr=[]
s=input()
while s!="over":
    arr.append(list(map(float,s.split())))
    s=input()
ave=[]
for i in arr:
    ave.append(sum(i)/len(i))
mu=sum(ave)/len(ave)
num=len(arr)*len(arr[0])
sigma=0
for i in arr:
    for j in i:
        sigma+=(j-mu)**2
sigma/=num
sigma**=0.5
if sigma==float(0):
    print("标准差为0，无法进行归一化。")
else:
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j]=(arr[i][j]-mu)/sigma
            print(f"{arr[i][j]:.2f}",end=" ")
        if i!=len(arr)-1:
            print("")
'''
'''
1 2 3 4
2 3 4 5.5
over

1 2 3 4.5
over
'''




import numpy as np
s=input()
s=list(map(float,s.split()))
arr=np.array([s])
s=input()
while s!="over":
    s=list(map(float, s.split()))
    s=np.array(s)
    arr=np.r_[arr,[s]]
    s=input()
std=np.std(arr)
mu=np.mean(arr)
row=arr.shape[0]
column=arr.shape[1]
if std==0:
    print("标准差为0，无法进行归一化。")
else:
    arr[:,:] = (arr[:,:] - mu) / std  # 第0列均值方差归一化
    # arr=np.around(arr,decimals=2)
    # print(arr)
    for i in range(row):
        for j in range(column):
            if j!=column-1:
                print(f"{arr[i][j]:.2f}", end=" ")
            else:
                print(f"{arr[i][j]:.2f}")



# #Pearson相关系数计算
# import numpy as np
# x=np.array(list(map(float,input().split())))
# y=np.array(list(map(float,input().split())))
# x_mean=np.mean(x)
# y_mean=np.mean(y)
# rxy=np.sum((x-x_mean)*(y-y_mean))/np.sqrt(np.sum(np.power((x-x_mean),2))*np.sum(np.power((y-y_mean),2)))
# print(f"{rxy:.2f}")

'''
-10.435470265909114 12.747031306749463 -9.221295835495077 -3.02711372992297 -18.17928122080451 5.135711062286312 -1.2368453242490958 12.139466399377213 -7.02329029607573 -4.1968533417462375 -14.375647698846983 -17.006665575491212 -10.902294500599655 -18.6164908148362 18.32668802209416 14.391382092076917 -2.753155583087544 13.591601171274384
-13.808546099831176 -0.7835921644261674 0.9974715674718269 -19.23923213273244 17.958701786403886 3.6791909946540926 8.552752339351166 19.033050678328635 -10.460769545823712 -4.649515915116629 -18.084814874034222 -10.373444430133993 2.098593339238267 -6.454123899938118 0.329804251292213 -11.457042521312978 6.382966255583881 6.232083334390573
'''




