a=pow(10,2,7)
b=pow(10,1.5)
print("b的值为：",b)
print("a的值为：",a)

'''
进制转换：bin()将给定的参数转换为二进制
        ort()将给定的参数转换为八进制
        hex()将给定的参数转换为十六进制
reversed()：将一个序列翻转，返回一个反向的迭代器，需要在使用序列再转换回去
bytes()：把字符串转化为bytes类型
repr()：repr原样输出，会过滤掉转义字符
sort()：默认为升序排序，若里面的参数reverse=True则降序排序
filter()：过滤器可以接收一个自定义筛选函数，将迭代器中的元素传到函数中进行判断，用来确定是否保留这个元素
next()：迭代器向下执行一次
iter()：获取迭代器
hash()：获取到hash值，用于做key
dir()：查看对象的内置属性

'''

# # 动态加载os模块os
# name = input("请输入你要导入的模块：")  # 输入os
# os = __import__(name)
# print(os.getcwd())
# import os
# print(os.getcwd())
# print(os.listdir(os.getcwd()))

