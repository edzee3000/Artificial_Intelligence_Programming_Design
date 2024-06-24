
''''''
'''
def log_params_and_result(func):
# 完成装饰器
    def wrapped(*args,**kwargs):
        name=func.__name__
        res=func(*args,**kwargs)
        args_list=[repr(ele) for ele in args]
        kwargs_list=[f"{k}={v}" for k,v in kwargs.items()]
        compose=args_list+kwargs_list
        print(compose)
        print_form=",".join(compose)
        print(f"调用 {name}({print_form}) -> {res}")
        return res
    return wrapped
@log_params_and_result
def add(a,b,num=0):
    return f"{a}+{b}={num}?",a+b
@log_params_and_result
def say_hello(name):
    return f"Hello, {name}!", f"你好，{name}!"
add(3,4,"7")
say_hello("Alice")
'''




