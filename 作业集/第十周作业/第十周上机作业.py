
class Cache:
    def __init__(self):
        self.memory={}
        pass# 删除这一行，并添加适当的代码,完成该类的构建
    def get(self,key):
        if key in self.memory.keys():
            return self.memory[key]
        else:
            return None
    def set(self,key,value):
        self.memory[key]=value
    def clear(self):
        self.memory={}
# Cache_fib=Cache()
# Cache_fac=Cache()
def fibonacci(n, cache):
    if n==1 or n==2:
        cache.set(1, 1)
        cache.set(2,1)
        return cache.get(n)
    if cache.get(n):
        return cache.get(n)
    else:
        cache.set(n,fibonacci(n-1,cache)+fibonacci(n-2,cache))
    return cache.get(n)
def factorial(n, cache):
    if n==1:
        cache.set(1,1)
        return 1
    elif n==2:
        cache.set(1,2)
        return 2

    if cache.get(n):
        '''如果n在键列表里面'''
        return cache.get(n)
    else:
        cache.set(n,n*factorial(n-1,cache))
    return cache.get(n)
#print(fibonacci(130,Cache()))
#print(factorial(30,Cache()))



#分数类Fraction构建
import math
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator=numerator
        self.denominator=denominator
        self.simplify()
        self.describe()
        pass# 删除这一行，并添加适当的代码,完成该类的构建
    def describe(self):
        if self.denominator==0:
            self.simplest_form="nan"
        else:
            self.simplest_form=f"{self.numerator}/{self.denominator}"
    def simplify(self):
        max_common=math.gcd(self.numerator,self.denominator)
        self.numerator//=max_common
        self.denominator//=max_common
    def __add__(self, other):
        ''''''
        if self.simplest_form=="nan"or other.simplest_form=="nan":
            return "nan"
        else:
            # min_common_num=math.lcm(self.denominator,other.denominator)
            n1=self.denominator
            n2=other.denominator
            res=Fraction(self.numerator*n2+other.numerator*n1,n1*n2)
            return res.simplest_form
    def __sub__(self, other):
        if self.simplest_form=="nan"or other.simplest_form=="nan":
            return "nan"
        else:
            # min_common_num=math.lcm(self.denominator,other.denominator)
            n1=self.denominator
            n2=other.denominator
            res=Fraction(self.numerator*n2-other.numerator*n1,n1*n2)
            return res.simplest_form
    def __mul__(self, other):
        if self.simplest_form=="nan"or other.simplest_form=="nan":
            return "nan"
        else:
            # min_common_num=math.lcm(self.denominator,other.denominator)
            n1=self.denominator
            n2=other.denominator
            res=Fraction(self.numerator*other.numerator,n1*n2)
            return res.simplest_form
    def __truediv__(self, other):
        if self.simplest_form=="nan"or other.simplest_form=="nan":
            return "nan"
        else:
            # min_common_num=math.lcm(self.denominator,other.denominator)
            n1=self.denominator
            n2=other.denominator
            res=Fraction(self.numerator*n2,n1*other.numerator)
            return res.simplest_form
# print(Fraction("0/3")/Fraction("2/5"))
#print(Fraction(0,3)/Fraction(2,5))



#简单异常处理练习
class NonIntegerError(Exception):
    def __init__(self, message="Input must be an integer"):
        self.message=message
        pass# 删除这一行，并添加适当的代码,完成该类的构建

def compute_square(value):
    # try:
    #     return value**2
    # except NonIntegerError():
    #     print(NonIntegerError().message)
    # else:
    #     print("An unexpected error occurred")
    #     pass
    # finally:
    #     pass
    # pass# 删除这一行，并添加适当的代码,完成该函数的构建
    if value != None and type(value) != int:
        raise NonIntegerError("Invalid input. Please enter a valid integer.")
    elif value != None and value < 0:
        raise NonIntegerError("Assertion Error: Value must be positive")
    else:
        raise NonIntegerError("An unexpected error occurred")




#实现DesignSet类
class DesignSet:
    def __init__(self):
        ''''''
        self.Set=[]
    def insert(self,val:int):
        if val in self.Set:
            return False
        else:
            self.Set.append(val)
            return True
    def remove(self,val:int):
        if val in self.Set:
            self.Set.remove(val)
            return True
        else:
            return False
    def get_all(self)->list:
        return self.Set




