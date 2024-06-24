


# Embedding Table
import numpy as np
np.set_printoptions(precision=2)

row,column=tuple(map(int,input().split()))
arr=np.ones((row,column),dtype=np.float32)
for i in range(row):
    l = np.array(tuple(map(float, input().split())))
    arr[i]=l
# index,b=tuple(map(int,input().split()))
# for i in range(b):
#     new_arr[i]=arr[index]
# new_arr=np.repeat([arr[index]],b,axis=0)
# print(new_arr)
print(arr[list((map(int,input().split())))])
'''
3 4
-0.63 1.75 -2.31 -0.07
-1.08 0.44 0.89 -0.99
0.84 -0.75 1.38 1.24
2 2

3 4
-0.63 1.75 -2.31 -0.07
-1.08 0.44 0.89 -0.99
0.84 -0.75 1.38 1.24
2 1
'''


"""
#
import numpy as np
def judge(m1,m2):
    '''m1与m2分别为两个列表'''
    n1=list(reversed(m1))
    n2=list(reversed(m2))
    l=min(len(n1),len(n2))
    a1 = n1 if l == len(n1) else n2  # 取最小的那个
    a2 = n2 if a1 == n1 else n1  # 取另一个
    if len(n1)!=len(n2):
        a1+=[1]*(len(a2)-len(a1))
    l=max(len(n1),len(n2))
    flag=True
    for i in range(l):
        if (a1[i]!=1 and a2[i]!=1) and a1[i]!=a2[i]:
            print("illegal")
            return
        elif a1[i]==1 and a2[i]!=1:
            flag=False
            a1[i]=a2[i]
        elif a2[i]==1 and a1[i]!=1:
            flag = False
            a2[i] = a1[i]
    if flag:
        print("legal")
        return
    else:
        print(("broadcast",tuple(reversed(a1))))
        return
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
judge(l1,l2)
'''
3 5 7
3 5 1
'''
"""



"""
#self-attention前向计算
import numpy as np
np.set_printoptions(precision=2)
def softmax(mat):
    '''以下实现softmax函数，最后返回结果为1*n的矩阵'''
    global n
    arr=np.ones((n,mat.shape[1]))
    for i in range(mat.shape[0]):
        sum_zj=np.exp(mat[i]).sum()
        yi=np.exp(mat[i])/sum_zj
        arr[i]=yi
    return arr
n,m=tuple(map(int,input().split()))
arr=np.ones((3*n,m),dtype=np.float32)
for i in range(3*n):
    arr[i]=np.array(list(map(float,input().split())))
Q,K,V=tuple(np.split(arr,3,axis=0))
QK=np.matmul(Q,K.T)/(m**0.5)
Attention=softmax(mat=QK)
out=np.matmul(Attention,V)
print(out)
'''
1 9
0.41 -2.02 1.00 0.68 -1.13 -1.34 -0.71 0.54 -0.10
-2.22 -1.68 -0.16 0.35 -0.04 0.13 -0.97 1.32 0.45
-0.18 -1.16 0.30 -1.23 0.08 0.05 0.08 1.08 0.15
'''
"""