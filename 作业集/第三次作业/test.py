# class Stu():
#     def __init__(self, name, age):
#         print("在__init__方法中", id(self))
#         self.name = name
#         self.age = age
#
#     def run(self):
#         print("在run方法中", id(self))
#         print("{name} is running".format(name=self.name))
#
#
# s1 = Stu('小明', 18)
# print("s1的内存地址", id(s1))
# s1.run()

# nums = [1, 2, 3]
# squares = [x**2 for x in nums]
# squares=iter(squares)
# print(squares)
#
# nums = [1, 2, 3]
# squares = (x**2 for x in nums)
# print(squares)
# print(list(squares))
#
# sum=0
# i=2
# while i<=100:
#     sum+=i
#     i+=2
# print("1到100以内所有偶数的和为：",sum)



# import os
# str_input=input("请输入要输入文件等等字符串：")
# with open("file_input.txt","w+") as f:
#     f.write(str_input)
# print("接下来进行读取并打印操作")
# with open("file_input.txt","r") as f:
#     contents=f.readlines()
#     for line in contents:
#         print(line)
# print("打印操作结束")


# a = input()
# b = input()
# c = b.split()
# count = 0
# for i in c:
#     if i.lower() == a.lower():
#         count += 1
#         position = b.find(i)
# if count > 0:
#      print(count, position)
# else:
#     print(-1)



# list1=[2,4,5,9]
# x=iter(list1)
# print("迭代器为：",x)
# print("迭代器指向第一个元素为：",next(x))
# for i in x:
#     print(i,end=" ")
# print("")
# print("迭代器x指向下一个元素：",next(x))

# list1=[2,4,5,9]
# x=(i*2 for i in list1)
# print("生成器为：",x)
# print("生成器指向第一个元素为：",next(x))
# for i in x:
#     print(i,end=" ")
# print("")
# print("生成器x指向下一个元素：",next(x))



# def generator():
#     list1=[2,4,5,9]
#     for i in list1:
#         yield i**2
#         print("当对生成器进行迭代的时候直接从yield下一行语句开始执行")
#         print("返回生成器当中多加一个元素：",i**2)
# x=generator()
# for i in x:
#     print(i,end="\t")


# num=int(input("请输入一个整数判断其正负性："))
# if num >0:
#     print("Positive")
# elif num==0:
#     print("Zero")
# else:
#     print("Negative")

''''''
import cmath

'''
#回文数
num=input("请输入一个自然数：")
list_num=list(num)
print(list_num)
while len(list_num)>1:
    if list_num[0]!=list_num[-1]:
        print("False")
        break
    else:
        list_num.pop(0)
        list_num.pop()
if len(list_num)<=1:
    print("True")
'''
'''
#+3之后的非空数组
list_num=eval(input("请输入一个正整数："))
num=0
for i in range(len(list_num)):
    num+=list_num[i]*10**(len(list_num)-i-1)
num=str(num+3)
list_num=[int(str_i) for str_i in list(num)]
print(list_num)'''


'''
#最大子字符串数量
str_input=input("请输入字符串：")
list_str=list(str_input)
num=0
num_mn=[0,0]#前一个为m，后一个为n
for i in list_str:
    if i=="m":
        num_mn[0]+=1
    elif i=="n":
        num_mn[1]+=1
    if num_mn[0]==num_mn[1]:
        num+=1
        num_mn=[0,0]
print(num)'''
'''
import math
str_input=input("")
a,b,c=map(float,str_input.split(" "))
x1=complex((-b-(b**2-4*a*c)**0.5)/(2*a))
x2=complex((-b+(b**2-4*a*c)**0.5)/(2*a))
print(x1,x2)
x1_real=int(math.floor(x1.real))
x1_imag=int(math.floor(x1.imag))
x2_real=int(math.floor(x2.real))
x2_imag=int(math.floor(x2.imag))
if x1_real<x2_real or x1_real==x2_real and x1_imag<x2_imag:
    if x1_imag >= 0 and x2_imag>=0:
        print(f"{x1_real}+{x1_imag}j {x2_real}+{x2_imag}j")
    elif x1_imag < 0 and x2_imag>=0:
        print(f"{x1_real}-{abs(x1_imag)}j {x2_real}+{x2_imag}j")
    elif x1_imag >= 0 and x2_imag < 0:
        print(f"{x1_real}+{x1_imag}j {x2_real}-{abs(x2_imag)}j")
    else:
        print(f"{x1_real}-{abs(x1_imag)}j {x2_real}-{abs(x2_imag)}j")
else:
    if x1_imag >= 0 and x2_imag>=0:
        print(f"{x2_real}+{x2_imag}j {x1_real}+{x1_imag}j")
    elif x1_imag < 0 and x2_imag>=0:
        print(f"{x2_real}-{abs(x2_imag)}j {x1_real}+{x1_imag}j")
    elif x1_imag >= 0 and x2_imag < 0:
        print(f"{x2_real}+{x2_imag}j {x1_real}-{abs(x1_imag)}j")
    else:
        print(f"{x2_real}-{abs(x2_imag)}j {x1_real}-{abs(x1_imag)}j")'''
# x1=complex(int(-b//(2*a)), (-delta/(2*a)))
# x2=complex(int(-b//(2*a)), (+delta/(2*a) ))
# x1=list(str(x1))
# x1.pop(0)
# x1.pop(-1)
# x1="".join(x1)
# x2=list(str(x2))
# x2.pop(0)
# x2.pop(-1)
# x2="".join(x2)
# print(x1,x2)
# judge=int(x1.imag)
# if judge==0:
#     print(f"{int(x1.real)}+0j {int(x2.real)}+0j")
# elif judge>0:
#     print(f"{int(x1.real)}+{int(x1.imag)}j {int(x2.real)}+{int(x2.imag)}j")
# else:
#     print(f"{int(x2.real)}-{abs(int(x2.imag))}j {int(x1.real)}-{abs(int(x1.imag))}j")
# x1_real=int(x1.real)
# x1_imag=int(x1.imag)
# x2_real=int(x2.real)
# x2_imag=int(x2.imag)
# judge=int(x1.imag)
# new_x1=complex(x1_real,x1_imag)
# new_x2=complex(x2_real,x2_imag)
#
# if judge==0:
#     if x1.real<x2.real:
#         print(f"{int(x1.real)}+0j {int(x2.real)}+0j")
#     else:
#         print(f"{int(x2.real)}+0j {int(x1.real)}+0j")
# elif judge>0:
#     if x1_real<x2_real or x1_real==x2_real and x1_imag<x2_imag:
#         print(f"{int(x1.real)}+{int(x1.imag)}j {int(x2.real)}+{int(x2.imag)}j")
#     else:
#         print(f"{int(x2.real)}+{int(x2.imag)}j {int(x1.real)}+{int(x1.imag)}j")
# else:
#     if x1_real < x2_real or x1_real == x2_real and x1_imag < x2_imag:
#         print(f"{int(x1.real)}-{abs(int(x1.imag))}j {int(x2.real)}-{abs(int(x2.imag))}j")
#     else:
#         print(f"{int(x2.real)}-{abs(int(x2.imag))}j {int(x1.real)}-{abs(int(x1.imag))}j")
# delta=cmath.sqrt((b**2-4*a*c))
# if delta==0:


#汉诺塔问题尝试
def Hannuota(num,tower1,tower2,tower3,dict1):
    '''汉诺塔问题递归  最终将所有的盘子移到tower3上'''
    if num==1:
        move(tower1,tower3)
        index_min=min(get_key(dict1,tower1))
        dict1[index_min]=tower3
        print(dict1)
    else:
        Hannuota(num-1,tower1,tower3,tower2,dict1)#将tower1上的num-1个盘子全都移到tower2上去
        move(tower1,tower3)#将tower1上那个盘子移到tower3上去
        index_min = min(get_key(dict1, tower1))
        dict1[index_min] = tower3
        print(dict1)
        Hannuota(num - 1, tower2, tower1,tower3,dict1)#将tower2上的num-1个盘子全都移到tower3上去
def move(t1,t2):
    """将t1上的盘子移到t2上去"""
    print(f"{t1}->{t2}")
def get_key(dict1,values):
    return [key for key in dict1 if dict1[key]==values]
#返回塔上最小的index索引
def return_min_index(dict1,values):
    return min([key for key in dict1 if dict1[key]==values])
#寻找起点与终点是否允许，不妨给每一个结点设置一个[所有的[[位置状态]，{移动一步相邻的位置状态组成的集合}]]
#注意需要考虑不能往回走可以走其余的塔
'''def new_hannota(num,tower1,tower2,tower3,dict1,dict1_state,have_move_index=-1):
    if num>=200:
        return
    if have_move_index==-1:#在最开始什么都没有动的时候
        dict1_copy=dict1.copy()
        
        print(f"{tower1}->{tower2}")
        index_min = min(get_key(dict1, tower1))
        dict1[index_min] = tower3
        print(dict1)
        dict1_state[0][1].add(dict1)
        new_hannota(num+1,tower1,tower2,tower3,dict1,dict1_state,have_move_index=0)
        
        print(f"{tower1}->{tower3}")
        index_min = min(get_key(dict1_copy, tower1))
        dict1_copy[index_min] = tower3
        print(dict1_copy)
        dict1_state[0][1].add(dict1_copy)
        new_hannota(num + 1, tower1, tower2, tower3, dict1_copy, dict1_state, have_move_index=0)
    else:
'''


list1=range(3)
dict1={}
for i in list1:
    dict1[i]="A"
#Hannuota(3,"A","B","C",dict1)
dict1_state=[[dict1,{}]]
#new_hannota(0,"A","B","C",dict1=dict1,dict1_state=dict1_state)