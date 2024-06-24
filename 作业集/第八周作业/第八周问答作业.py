''''''
'''高阶函数处理列表数据——假设要实现对向量x实现y=Ax+b的操作得到y向量'''
#一个通用的高阶函数框架如下
def higher_func(func_input):
    def wrapped(list_input):
        res=func_input(list_input)
        return res
    return wrapped
#接下来写y=Ax+b的功能
def linear_transformation(A,x):
    '''实现A*x操作 前提是A与x一定得是同维的'''
    y=[]
    for i in A:
        sum=0
        for j in range(len(i)):
            sum+=i[j]*x[j]
        y.append(sum)
    return y
def add_vector(x,b):
    '''实现向量相加的运算 前提是x和b一定是同维的'''
    return [x[i]+b[i] for i in range(len(x))]
def x_to_y(func1):
    def wrapped_1(func2):
        def wrapped_2(list_input,A,b):
            res1=func1(A,list_input)
            res2=func2(res1,b)
            return res2
        return wrapped_2
    return wrapped_1
A=[[1,0,0],
   [0,2,0],
   [0,0,1]]
b=[1,2,3]
x=[2,3,4]
y=x_to_y(linear_transformation)(add_vector)(x,A,b)
print(y)





'''医生工作状态
class GetSwitcher:
    ''''''
    def __init__(self,name):
        ''''''
        self.name=name
        self.state="空闲"
    def switch(self):
        if self.state=="空闲":
            self.state="忙碌"
        else:
            self.state="空闲"
        print(f"{self.name}医生当前状态为：{self.state}")

sw1 = GetSwitcher("Sun")  #为孙医生建立一个sw，初始为空闲
sw1.switch() #切换状态，原先为空闲则改为忙碌，反之亦然；输出当前状态
sw1.switch() #再次切换状态，原先为空闲则改为忙碌，反之亦然；输出当前状态
sw2 = GetSwitcher("Zhang") #为张医生建立一个sw ...
sw2.switch()'''



















'''医生工作状态修改版
def createDoctorStatusTracker(name):
    ''''''
    state="空闲"
    def wrapped(str_input):
        ''''''
        nonlocal state
        if str_input=="state":
            print(f"{name}医生当前的状态为：{state}")
        elif str_input=="switch":
            if state=="空闲":
                state="忙碌"
            else:
                state="空闲"
            print(f"{name}医生当前的状态为：{state}")
    return wrapped
dr_sun = createDoctorStatusTracker("Sun")  # 为孙医生创建一个状态跟踪器，初始状态为“空闲”
dr_sun("state") # 查询当前医生工作状态
dr_sun("switch") # 切换状态，如果原先为空闲则改为忙碌，反之亦然，并输出新的状态print(dr_sun()) # 再次查询当前状态，输出更新后的状态
dr_zhang = createDoctorStatusTracker("Zhang") # 为张医生创建一个状态跟踪器 ...
dr_zhang("switch") # 切换张医生的状态并输出...'''







