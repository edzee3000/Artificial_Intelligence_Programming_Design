import copy
class N_matric:
    def __init__(self,array):
        self.array=array
        self.cal_dim()
        self.to_one_array()#将高维数组展平
        self.cal_trace()
    def cal_dim(self):
        '''计算self.array的维数大小、shape形状以及strides元组大小'''
        dim=1
        a=self.array
        num=1
        while type(a[0])==list:
            num*=len(a)
            dim+=1
            a=a[0]
        print("数组的维数为：",dim)
        self.dim=dim#存储矩阵维数大小
        num*=len(a)
        self.num=num#存储数组拥有的元素个数
        print("数组拥有的元素个数为：",num)
        '''接下来模仿numpy当中操作计算strides序列'''
        strides=[0]*self.dim
        shape=[0]*self.dim
        i=0
        a = self.array
        while type(a[0])==list:
            shape[i]=len(a)
            a = a[0]
            strides=[j*len(a) for j in strides]
            strides[i] = len(a)
            i+=1
        strides[self.dim-1]=1
        shape[i]=len(a)
        self.strides=strides#存储数组的strides访问时移动的个数
        self.shape=shape#存储数组的shape形状大小
        print("数组的形状大小为：",self.shape)
        print("数组的strides为：",strides)
    def to_one_array(self):
        '''将高维数组展成一维数组'''
        def one_array(array):
            ''''''
            if type(array[0])!=list:
                return array
            else:
                total=[]
                for sub_arr in array:
                    total+=one_array(sub_arr)
                return total
        self.array=one_array(self.array)
        print("将数组展平之后为：",self.array)
    def visit_element(self,*args):
        '''元素访问，传入未知个数元组，表示各个维度的索引'''
        if len(args)>self.dim:
            print("注意！您访问的元素超出了维度限制")
            return None
        # ele=self.array[args[0]]#被注释掉的代码是没有将高维数组展平
        # for i in range(1,len(args)):
        #     ele=ele[args[i]]
        ele=0
        for i in range(len(args)):
            ele+=self.strides[i]*args[i]
        return self.array[ele]
    def Reshape(self,new_shape):
        '''注意new_shape传进来的是一个元组'''
        multiplication=1
        for i in new_shape:
            multiplication*=i
        if multiplication!=self.num:
            print("传入的重塑数组形状大小有误")
            raise Exception("改变前后的元素总数不一致")
            return
        strides=[0]*self.dim
        for i in range(1,len(new_shape)):
            strides[i-1]=1
            strides=[j*new_shape[i] for j in strides]
        strides[len(new_shape)-1]=1
        self.strides=strides
        self.shape=list(new_shape)
        print(f"接下来进行数组形状重塑为{new_shape}操作")
        print("新的数组形状大小为：",new_shape)
        print("新的strides为：",self.strides)
    def transpose(self):
        '''对于更高维的数组直接倒序即可'''
        # self.Reshape(tuple(reversed(self.shape)))
        self.shape=list(reversed(self.shape))
        self.strides=list(reversed(self.strides))
    def __add__(self, other):
        '''矩阵加法，对应元素直接相加即可，并且要求数组是二维的'''
        if self.shape!=other.shape:
            print("两个数组形状不一致无法进行相加")
            return
        if self.dim!=2:
            print("矩阵运算要求数组是二维的")
            return
        new_array = [[0] * self.shape[1] for i in range(self.shape[0])]
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                new_array[i][j] = self.visit_element(i, j) + other.visit_element(i, j)
        return N_matric(new_array)
    def __sub__(self, other):
        if self.shape!=other.shape:
            print("两个数组形状不一致无法进行相加")
            return
        if self.dim!=2:
            print("矩阵运算要求数组是二维的")
            return
        new_array=[[0]*self.shape[1] for i in range(self.shape[0])]
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                new_array[i][j]=self.visit_element(i,j)-other.visit_element(i,j)
        return N_matric(new_array)
    def dotmul(self,other):
        if self.shape!=other.shape:
            print("两个数组形状不一致无法进行相加")
            return
        if self.dim!=2:
            print("矩阵运算要求数组是二维的")
            return
        new_array=[[0]*self.shape[1] for i in range(self.shape[0])]
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                new_array[i][j]=self.visit_element(i,j)*other.visit_element(i,j)
        return N_matric(new_array)
    def __mul__(self, other):
        if self.shape[1]!=other.shape[0]:
            print("两个数组形状不一致无法进行相加")
            return
        if self.dim!=2:
            print("矩阵运算要求数组是二维的")
            return
        new_array = [[0]*other.shape[1] for i in range(self.shape[0])]
        for i in range(self.shape[0]):
            for j in range(other.shape[1]):
                sum=0
                for h in range(self.shape[1]):
                    sum+=self.visit_element(i,h)*other.visit_element(h,j)
                new_array[i][j]=sum
        return N_matric(new_array)
    def cal_trace(self):
        '''求方阵的迹'''
        if self.shape[0]!=self.shape[1]:
            print("非方阵不可求迹")
            return
        sum=0
        for i in range(self.shape[0]):
            sum+=self.visit_element(i,i)
        self.trace=sum
        return self.trace

arr=[[[1,2,3],
      [4,5,6]],
     [[7,8,9],
      [10,11,12]],
     [[13,14,15],
      [16,17,18]]]
arr1=[[[[1,2,3],
      [4,5,6]],
     [[7,8,9],
      [10,11,12]],
     [[13,14,15],
      [16,17,18]]],
      [[[[1,2,3],
      [4,5,6]],
     [[7,8,9],
      [10,11,12]],
     [[13,14,15],
      [16,17,18]]]]]
arr2=[[1,2,3],
      [4,5,6]]
arr3=[[0,1,2],
      [3,4,5]]
print("先展示二维数组：")
print("arr2数组为：",arr2)
arr2=N_matric(arr2)
print("arr2坐标(2,3)的元素为：",arr2.visit_element(1,2))
arr2.transpose()
print("将arr2转置后坐标(1,2)的元素为：",arr2.visit_element(0,1))
print("将arr2转置后坐标(3,1)的元素为：",arr2.visit_element(2,0))
arr2.Reshape((1,6))
print("将arr2重塑为行向量后坐标(1,6)的元素为：",arr2.visit_element(0,5))
arr2.Reshape((6,1))
print("将arr2重塑为列向量后坐标(6,1)的元素为：",arr2.visit_element(5,0))

print("")
print("接下来再展示三维数组：")
arr=N_matric(arr)
print("arr坐标(2,2,2)的元素为：",arr.visit_element(1,1,1))
arr.transpose()
print("将arr转置后坐标(2,2,2)的元素为：",arr.visit_element(1,1,1))
arr.Reshape((2,3,3))
print("将arr重塑为(2,3,3)后坐标(1,2,3)的元素为：",arr.visit_element(0,1,2))
arr.Reshape((3,3,2))
print("将arr重塑为(3,3,2)后坐标(1,2,3)的元素为：",arr.visit_element(0,1,2))
#注意这里因为超出元素访问界限因此会有提示！！！
print("将arr重塑为(3,3,2)后坐标(1,2,1)的元素为：",arr.visit_element(0,1,0))

print("")
print("接下来再展示四维数组：")
arr1=N_matric(arr1)
print("arr1坐标(2,2,2,2)的元素为：",arr1.visit_element(1,1,1,1))
arr.transpose()
print("将arr转置后坐标(1,2,1,2)的元素为：",arr1.visit_element(0,1,0,1))

print("")
print("接下来展示矩阵运算操作")
arr2.Reshape((2,3))
arr3=N_matric(arr3)
print("")
print("矩阵加法结果为：",(arr2+arr3).array)
print("")
print("矩阵减法结果为：",(arr2-arr3).array)
print("")
print("矩阵点乘结果为：",arr2.dotmul(arr3).array)
print("")
arr2.transpose()
three_dim_phalanx=(arr2*arr3)
print("arr2*arr3矩阵乘法结果为：",three_dim_phalanx.array)
print("arr2*arr3为方阵其迹为：",three_dim_phalanx.trace)
print("")
two_dim_phalanx=(arr3*arr2)
print("arr3*arr2矩阵乘法结果为：",two_dim_phalanx.array)
print("arr3*arr2为方阵其迹为：",two_dim_phalanx.trace)