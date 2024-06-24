
from typing import Any
from typing import *

def compose(func_input:Any) -> int :
    def wrapped(*args,**kwargs):
        res=func_input(*args,**kwargs)
        return res
    return wrapped

res=compose(lambda x:x*2)(6)
# print(res)

def funcDiv(x , y):
    if y != 0:
        return x/y
    else:
        raise Exception("div-zero")
def data_processing(x, y, comp):
    return comp(x, y)
def compute(x, y):
    return funcDiv(y, x) + funcDiv(x, y)
# data_processing(1, 0, compute)



class Student:
    def __init__(self,name,grades):
        self.name=name
        self.grades=grades
    def add_grade(self,grade):
        self.grades.append(grade)
    def calculate_average(self):
        if len(self.grades)==0:
            return 'nan'
        else:
            return sum(self.grades)/len(self.grades)
class Classroom:
    def __init__(self,students):
        self.students=students
    def add_student(self,student):
        self.students.append(student)
    def calculate_class_average(self):
        if len(self.students)==0:
            return 'nan'
        else:
            grades=[i.calculate_average() for i in self.students]
            if "nan" in grades:
                return "nan"
            else:
                return sum(grades)/len(self.students)
n=input()
students=[]
while n !='over':
    mylist=n.split()
    grades=[float(mylist[i]) for i in range(1,len(mylist))]
    student=Student(mylist[0],grades)
    students.append(student)
    n=input()
classroom=Classroom(students)
for i in students:
    if i.calculate_average()=='nan':
        print(i.name,i.calculate_average())
    else:
        print(i.name,'{0:.2f}'.format(i.calculate_average()))
if classroom.calculate_class_average()=='nan':
    print('classroom',classroom.calculate_class_average())
else:
    print('classroom','{0:.2f}'.format(classroom.calculate_class_average()))