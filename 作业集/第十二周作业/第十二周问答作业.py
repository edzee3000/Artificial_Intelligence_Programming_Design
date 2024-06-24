


import numpy as np
import time
import timeit
# def row_visit(arr):
#     '''行主序'''
#     for i in arr:
#         for j in i:
#             j
# def column_visit(arr):
#     '''列主序'''
#     for i in range(len(arr[0])):
#         for j in range(len(arr)):
#             arr[j][i]
# arr=np.random.randn(10000,10000)
# time_row = timeit.timeit('row_visit(arr)', 'from __main__ import row_visit,arr', number=1)
# time_column=timeit.timeit('column_visit(arr)', 'from __main__ import column_visit,arr', number=1)
# print(f"row_visit took {time_row} seconds to complete.")
# print(f"column_visit took {time_column} seconds to complete.")
# arr=[[[[1,2],[3,4],[5,6],[7,8],[9,10]],
#       [[1,2],[3,4],[5,6],[7,8],[9,10]],
#       [[1,2],[3,4],[5,6],[7,8],[9,10]],
#       [[1,2],[3,4],[5,6],[7,8],[9,10]]],
#      [[[1,2],[3,4],[5,6],[7,8],[9,10]],
#       [[1,2],[3,4],[5,6],[7,8],[9,10]],
#       [[1,2],[3,4],[5,6],[7,8],[9,10]],
#       [[1,2],[3,4],[5,6],[7,8],[9,10]]],
#      [[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],
#       [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],
#       [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],
#       [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]]]
# #arr为(3,4,5,2)的数组
# arr=np.mean(arr,axis=0)#arr变为(4,5,2)的数组
# print(arr)
# arr=np.random.uniform(0,1,(100,))
# print("数组的平均值为：",arr.mean())
# print("数组的总和为：",arr.sum())
# print("数组的最大值为：",arr.max())
# print("数组的最小值为：",arr.min())
# arr=np.random.randint(1,100,size=(10,10))
# print("所有大于50元素的标准差为：",arr[arr>50].std())


class ThreeDimMatrix:
    def __init__(self,depth,rows,columns):
        '''初始化三维数组'''
        self.depth=depth
        self.rows=rows
        self.columns=columns
        self.arr=np.random.randint(0,10000,size=(depth,rows,columns))
    def slice(self,start,end,step=[1,1,1]):
        '''切片操作 其中start、end、step对应三个切片，step可以缺失默认为1'''
        step+=[1]*(3-len(step))
        return self.arr[start[0]:end[0]:step[0],
               start[1]:end[1]:step[1],
               start[2]:end[2]:step[2]]
    def verify_view(self):
        '''通过slice方法得到视图，对视图进行修改，查看结果'''
        # a=np.random.randint(0, self.depth, (2,))
        # a.sort()
        # a1,b1=tuple(a)
        # b = np.random.randint(0, self.rows, (2,))
        # b.sort()
        # a2, b2 = tuple(b)
        # c = np.random.randint(0, self.columns, (2,))
        # c.sort()
        # a3, b3 = tuple(c)
        # print(a,b,c)
        # s=self.slice((a1,a2,a3),(b1,b2,b3))
        s = self.slice((1, self.rows//3, self.columns//2),
                       (self.depth-1, self.rows-1, self.columns))
        print("在verify_view()函数当中随机矩阵切片为：",s)
        print("接下来将切片中所有元素置0")
        s[:,:,:]=0
        print("将切片元素置为0后原来数组为：",self.arr)
matrix=ThreeDimMatrix(6,6,7)
print("原始矩阵为：",matrix.arr)
s=matrix.slice([0,2,1],[2,4,4],[1,2,1])
print("经过第一次矩阵切片后为：",s)
s[:,:,:]=0
print("对切片进行修改后值为：",matrix.arr)
# matrix.verify_view()
s=matrix.slice([0,1,0],[3,2,4])
print("经过第二次矩阵切片后为：",s)
s[:,:,:]=0
print("对切片进行修改后值为：",matrix.arr)
s=matrix.slice([2,0,1],[7,4,7])
print("经过第三次矩阵切片后为：",s)
s[:,:,:]=0
print("对切片进行修改后值为：",matrix.arr)