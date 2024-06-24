''''''


#一、列表拼接
'''
list1=eval(input())
list2=eval(input())
new_list=list1+list2
num_element=len(new_list)
for i in range(num_element):
    if i==num_element-1:
        print(new_list[i])
        break
    print(f"{new_list[i]}*",end="")
'''


'''
#二、列表操作
receive_list=eval(input())
new_list=[]
for num in receive_list:
    if num%2!=0:
        new_list.append(num**2)
new_list.sort(reverse=False)#.sort()方法里面记住False是升序
print(new_list)
'''

#三、评委打分   从大到小的顺序排序。
'''#用Decimal方法传进去字符串类型进行十进制的小数保留
from decimal import Decimal
receive_list=eval(input())
receive_list.sort(reverse=True)
receive_list.pop(len(receive_list)-1)
receive_list.pop(0)
mean=sum(receive_list)/len(receive_list)
print(round(Decimal(f"{mean}"),2))
print(receive_list)
'''
'''#问题出在哪：输出的时候不能按照round输出，需要格式化输出f"{mean:.2f}"表示输出到2位小数
#或者采用format格式化方法"{:.2f}".format(mean)
from decimal import Decimal
receive_list=eval(input())
receive_list.sort(reverse=True)
receive_list.pop(len(receive_list)-1)
receive_list.pop(0)
mean=sum(receive_list)/len(receive_list)
mean=round(mean,2)
print(f"{mean:.2f}")
print("{:.2f}".format(mean))
print(receive_list)
'''
'''
#四、字符排序
receive_string=input()
receive_string=set(receive_string)
list1=[]
for i in receive_string:
    if i!=" ":
        list1.append(i)
list1.sort()
new_string=""
for i in list1:
    new_string+=i
print(new_string)
'''
