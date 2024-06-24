


#序列计算模型
"""
def compose(input_func):
    '''compose函数接受每层计算函数组合起来'''
    def g(input_value1,input_value2):
        ''''''
        return input_func(input_value1,input_value2)
    return g
'''+ - * /
1 2 3 4
2
'''
symbol_dic={"+":lambda x,y:x+y,
             "-":lambda x,y:x-y,
             "*":lambda x,y:x*y,
             "/":lambda x,y:x/y}
symbol_list=input("请输入运算符：").split()
print("运算符为：",symbol_list)
num_list=list(map(int,input("请输入运算数：").split()))
print("运算数为：",num_list)
init_num=int(input("请输入初始值："))
func_list=[]
for i in range(len(symbol_list)):
    new_func=compose(symbol_dic[symbol_list[i]])#传进去lambda函数
    init_num=new_func(init_num,num_list[i])
print("最终结果为：",round(init_num,2))
"""


'''
bob 85 99 79
alice 30 87.5 45
over
bob
alice 30 87.5 45
over
'''

"""
from functools import reduce
class Student:
    def __init__(self,name,grades):
        self.name=name
        self.grades=grades
    def add_grade(self,grade):
        self.grades.append(grade)
    def calculate_average(self):
        if "nan" in self.grades:
            self.average="nan"
        else:
            self.average=reduce(lambda x,y:x+y,self.grades)/len(self.grades)
        return self.average
class Classroom:
    def __init__(self,students):
        self.students=students
    def add_student(self,student):
        self.students.append(student)
    def calculate_class_average(self):
        grades=[i.average for i in self.students]
        if "nan" in grades or grades==[]:
            self.average="nan"
        else:
            self.average=reduce(lambda x,y:x+y,grades)/len(grades)
        return self.average
s=input()
stu=[]
while s!="over":
    inf=s.split()
    grades = [float(inf[i]) for i in range(1, len(inf))]
    student=Student(inf[0],grades)
    stu.append(student)
    if len(inf)==1:
        student.average="nan"
    else:
        student.calculate_average()
    s=input()
for student in stu:
    if student.average=="nan":
        print(f"{student.name} nan")
    else:
        print(f"{student.name} {student.average:.2f}")
class1=Classroom(stu)
class1.calculate_class_average()
if class1.average=="nan":
    print(f"classroom nan")
else:
    print(f"classroom {class1.average:.2f}")
"""


'''
5 3|4 9 4|7
3|4 4|3 5 7 7|8
'''
"""
import math
from math import pi
#几何图形计算
class Shape:
    def __init__(self):
        ''''''
    def area(self):
        ''''''
class Rectangle(Shape):
    #super().__init__()
    def __init__(self,length,width):
        ''''''
        self.length=length
        self.width=width
        self.perimeter()
        self.area()
    def perimeter(self):
        self.peri=(self.length+self.width)*2
    def area(self):
        self.size=self.length*self.width
class Circle(Shape):
    #super().__init__()
    def __init__(self,radius):
        ''''''
        self.radius=radius
        self.perimeter()
        self.area()
    def perimeter(self):
        self.peri=2*pi*self.radius
    def area(self):
        self.size=pi*self.radius**2
s=input("请输入一行:").split()
for i in s:
    ''''''
    if "|" in i:#表明是长方形
        nums=list(map(float,i.split("|")))
        rec=Rectangle(nums[0],nums[1])
        print(f"{rec.size:.2f} {rec.peri:.2f}")
    else:#表明是圆
        r=int(i)
        cir=Circle(r)
        print(f"{cir.size:.2f} {cir.peri:.2f}")
"""



'''
alice
rw
alice|rwx chmod|alice|rwx alice|rwx
alice bob Edison
rw r rx
alice|rwx chmod|alice|rwx alice|rwx bob|rw Edison|wx
'''
"""
#权限管理器
def Decoration(func):
    def wrapped(*args,**kwargs):
        ''''''
        res=func(*args,**kwargs)
        return res
    return wrapped
@Decoration
def Read(name,right):
    '''读取函数'''
    if "r" in right:
        print(name,"read")
    else:
        print(name,fixed_str,"read")
@Decoration
def Write(name,right):
    '''读取函数'''
    if "w" in right:
        print(name,"write")
    else:
        print(name,fixed_str,"write")
@Decoration
def Execute(name,right):
    '''读取函数'''
    if "x" in right:
        print(name,"exec")
    else:
        print(name,fixed_str,"exec")
class Right:
    def __init__(self,name,right):
        self.name=name
        self.right=right
names=input("请输入人名：").split()
init_rights=input("请输入对应权限").split()
operations=input("请输入操作序列").split()
fixed_str="does not have the right to perform"
right_dict={names[i]:init_rights[i] for i in range(len(names))}
for i in operations:
    if "chmod" not in i:
        line=i.split("|")
        name=line[0]
        ope=line[1]
        right=right_dict[name]
        for j in ope:
            if j=="r":
                Read(name,right)
            elif j=="w":
                Write(name, right)
            elif j=="x":
                Execute(name, right)
    else:
        line = i.split("|")
        name = line[1]
        ope = line[2]
        right_dict[name]=ope
"""


def curry(fn):
    def curried(*args):
        if type(args[0])==function:
            return curry(args[0])
        else:
            return fn(*args)
    return curried
symbol_dic={"+":lambda x,y:x+y,
             "-":lambda x,y:x-y,
             "*":lambda x,y:x*y,
             "/":lambda x,y:x/y}
'''+ - * /
1 2 3 4
2
'''
# symbol_list=input("请输入运算符：").split()
# print("运算符为：",symbol_list)
# num_list=list(map(int,input("请输入运算数：").split()))
# print("运算数为：",num_list)
# init_num=int(input("请输入初始值："))

symbol_list=input("请输入运算符：").split()
init_func=symbol_list[0]
for i in range(len(symbol_list)):
    init_func=curry(symbol_dic[symbol_list[i]])#传进去lambda函数
    init_func=init_func()


# for i in range(len(symbol_list)):
#     new_func=compose(symbol_dic[symbol_list[i]])#传进去lambda函数
#     init_num=new_func(init_num,num_list[i])
# print("最终结果为：",round(init_num,2))
