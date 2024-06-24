# import numpy as np
# def process_four_dim_array(M, N, K, T, input_array):
#     pass  # 删除这一行，并添加适当的代码,完成该函数的编写
#     input_array = np.array(input_array).reshape(3, 4, M, N)
#     sub_arr = input_array[:2, :, :, :]
#     # sub_arr *= (K + 1)
#     sub_arr += sub_arr*K
#     input_array[input_array<T] = 0
#     s = input_array.sum()
#     ma = input_array.max()
#     mi = input_array.min()
#     print(f"{s:.4f}")
#     print(f"{ma:.4f}")
#     print(f"{mi:.4f}")
#
#
# M,N=tuple(map(int,input().split()))
# K=float(input())
# T=float(input())
# arr=np.array(list(map(float,input().split())))
# process_four_dim_array(M, N, K, T, arr)

'''
2 3
1.5
0.2
0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0 1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2.0 2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9 3.0 3.1 3.2 3.3 3.4 3.5 3.6 3.7 3.8 3.9 4.0 4.1 4.2 4.3 4.4 4.5 4.6 4.7 4.8 4.9 5.0 5.1 5.2 5.3 5.4 5.5 5.6 5.7 5.8 5.9 6.0 6.1 6.2 6.3 6.4 6.5 6.6 6.7 6.8 6.9 7.0 7.1 7.2
'''






import numpy as np
np.set_printoptions(precision=2)
def matrix_operation(matrix):
    matrix=np.array([[4,2,3],[3,1,5],[6,4,2]])
    det=np.linalg.det(matrix)
    print(f"{det:.2f}")
    eigval,eigvec=np.linalg.eig(matrix)#返回两个ndarray构成的一个元组，分别代表特征值与特征向量
    if (eigval>0).all()==True:
        print(True)
    else:
        print(False)
    eigval.sort()
    print_one_dim(eigval)
    if det==0:
        print("Matrix is not invertible")
    else:
        inv=np.linalg.inv(matrix)
        print(inv)
        print_ndarray(inv)
def print_ndarray(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j!=len(matrix[i])-1:
                print(f"{matrix[i][j]:.2f}",end=" ")
            else:
                print(f"{matrix[i][j]:.2f}")
def print_one_dim(arr):
    for i in range(len(arr)):
        if i != len(arr) - 1:
            print(f"{arr[i]:.2f}", end=" ")
        else:
            print(f"{arr[i]:.2f}")
matrix_operation(None)
















