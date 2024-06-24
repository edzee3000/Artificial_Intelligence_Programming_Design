


# #函数复合
# def compose(guess, checker, val):
# # 参数guess和checker是预测和检查函数，val是准确答案
# # 要输出最后预测值
#     ''''''
#     x=1
#     while not checker(x,val):
#         x=guess(x)
#     return x
#     # x=1
#     # for i in range(1,11,1):
#     #     if checker(x,val):
#     #         return x
#     #     x=guess(x)
# def guess(x):
# # 参数x是上一次的预测值
# # 要返回新的预测
#     ''''''
#     return x+1
# def checker(x, y):
# # x是预测值，y是准确答案
# # 要检查预测是否准确，
# # 返回布尔值True或False
#     if x==y:
#         return True
#     else:
#         return False
#
# print(compose(guess=guess,checker=checker,val=int(input())))




# typing import List
# def seven_pass(nums: List[int]) -> List[int]:
#     """
#     :param nums: List[int] 列表数据结构给定的数组
#     Return
#      List[int] 返回过滤后的数组
#     """
#     """ Write your code here"""
#     # return list(filter(lambda x:'7' not in str(x) and x%7!=0,nums))
#     return list(filter(remove_7, nums))
# def remove_7(x):
#     if '7' not in str(x) and x%7!=0:
#         return True
# print(seven_pass(eval(input())))


# from typing import List
# from functools import reduce
# def filter_and_sum(nums: List[int]) -> int:
#     num=reduce(lambda x,y:x+y,list(filter(lambda x:x>20,[i*2 for i in nums])))
#     return num
# print(filter_and_sum(eval(input())))



#装饰器函数
import inspect
#原因似乎是因为python版本过高，目前github上也有人提出了这个问题，但作者还没有对该问题进行修改。
#即在用到inspect这个包的代码里加上以下内容，这样就不会再报错了，也不会影响正常使用：
if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec
def log_params_and_result(func):
# 完成装饰器
#     argspec = inspect.getargspec(func)
#     argslist=argspec.args
#     argstr=", ".join(argslist)
#     print(f"调用 {func.__name__}({argstr}) -> ()",repr(func))
    def wrapper(*args, **kwargs):
        # 获取函数名
        func_name = func.__name__
        # 获取并格式化参数
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        arguments = ", ".join(args_repr + kwargs_repr)
        # 调用函数并获取结果
        result = func(*args, **kwargs)
        # 打印日志信息
        print(f"调用 {func_name}({arguments}) -> {repr(result)}")
        return result
    return wrapper


@log_params_and_result
def add(a, b):
    return a + b
@log_params_and_result
def say_hello(name):
    return f"Hello, {name}!", f"你好，{name}!"
add(3,4)
say_hello("edzee3000")