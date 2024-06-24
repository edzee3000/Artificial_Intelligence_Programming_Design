#创建字典
# dictionary={"num":1,"name":"Edison","age":19,"hobby":"rock"}
# print(dictionary)
# dict1=eval(input("请输入一个字典："))
# print(f"输入的字典为：{dict1}")



# a = [['_'] * 3 for i in range(3)]
# a[1][2] = 'X'
# print(a)#会输出[['_','_','_'],['_','_','X'],['_','_','_']]
#
# a = [['_'] * 3] * 3
# a[1][2] = 'X'
# print(a)#会输出[['_','_','X'],['_','_','X'],['_','_','X']]
#
#
# a,*b,c=[1,2,3,4]
# print(b)

# import timeit
#
# list1=[1,2,3,4]
# tuple1=(1,2,3,4)
# time_of_set_list=timeit.timeit("new_list=[i*2 for i in [1,2,3,4]]")
# time_of_set_tuple=timeit.timeit("new_tuple=(i*2 for i in (1,2,3,4))")
# timelist=timeit.timeit("[1,2,3,4]")
# timetuple=timeit.timeit("(1,2,3,4)")
# print("创建列表需要的时间为：",time_of_set_list)
# print("创建元组需要的时间为：",time_of_set_tuple)
# print("创建列表需要的时间为：",timelist)
# print("创建元组需要的时间为：",timetuple)
# new_tuple=(i*2 for i in (1,2,3,4))
# print(new_tuple)#tuple不可以用解析直接生成，返回的是一个迭代器



import os
with open(r"E:\大学课程\大一下\人工智能程序设计\作业集\第三次作业\catch.html") as html:
    content=html.readlines()
    content_to_list=[line.strip() for line in content if line!="\n"]
    print(content_to_list)
    content_to_list=[line.strip().split('<').pop().split(">").pop(0)
                     for line in content_to_list if line!='']
    print(content_to_list)
    content_to_list=[line.split(' ')
                     for line in content_to_list]
    content_to_list=[word for line in content_to_list for word in line]
    content_to_list=[line.split('=')
                     for line in content_to_list if line!='']
    content_to_list = [word for line in content_to_list for word in line]
    content_to_list = [line.strip('\"')
                       for line in content_to_list]
    print(content_to_list)
    for line in content_to_list:
        if type(line)==str:
            print("yes",end=" ")
    print("")
    dict1={}
    for line in content_to_list:
        if line not in dict1.keys():
            dict1[line]=1
        else:
            dict1[line]+=1
    print(dict1)
    max_num=0
    list_max=[]
    for key in dict1.keys():
        if dict1[key]<max_num:
            continue
        elif dict1[key]==max_num:
            list_max.append(key)
        else:
            list_max=[key]
            max_num=dict1[key]
    print("该html文件中存在最多的词为：",list_max)
    print("存在最多词个数为：",max_num)
'''
迭代器与列表的区别在于，构建迭代器的时候，不像列表把所有元素一次性加载到内存，
而是以一种延迟计算（lazy evaluation）方式返回元素，这正是它的优点。
比如列表中含有一千万个整数，需要占超过100M的内存，而迭代器只需要几十个字节的空间。
因为它并没有把所有元素装载到内存中，而是等到调用next()方法的时候才返回该元素
（按需调用 call by need 的方式，本质上 for 循环就是不断地调用迭代器的next()方法）
'''



