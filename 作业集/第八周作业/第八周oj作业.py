


'''
def cal_all_i_sum(num,total,func):
    ''''''
    sum=0
    for i in range(1,total+1):
        sum+=func(i,num)
    return sum
num=int(input("请输入一个正整数:"))
for i in range(1,num+1):
    ''''''
    sum=cal_all_i_sum(i,num,lambda x,i: x**i)
    print(sum)
'''



'''整数翻译
'''
import math
def English_explanation(str_input,num):
    '''num表示里面有几个Billion'''
    s=""
    str_list=str_to_list(str_input)#将str转化为列表
    #print(str_list)
    dict_list=[None]*4#每一段对应的英文表示
    for i in range(4):
        if str_list[i]==None:
            dict_list[i]=None
        else:
            dict_list[i]=sanweishu(str_list[i])
    #print(dict_list)
    for i in range(len(str_list)):
        if str_list[i]==None:
            continue
        else:
            if i==0:
                dict_list[i]+=" Billion"
            if i==1:
                dict_list[i]+=" Million"
            if i==2:
                dict_list[i]+=" Thousand"
            dict_list[i]+=" Billion"*num
    s=" ".join([v for v in dict_list if v!=None])
    #print(s)
    return s
def str_to_list(str_input):
    '''小于等于9位数转为list'''
    strlist=[]
    len_str=len(str_input)
    #print(len_str)
    a = len_str % 3
    if a==0:
        a=3
    if len_str > 9:
        strlist.append(str_input[0:a])
        strlist.append(str_input[a:a + 3])
        strlist.append(str_input[a + 3:a + 6])
        strlist.append(str_input[a + 6:a + 9])
    elif len_str>6:
        strlist.append(None)
        strlist.append(str_input[0:a])
        strlist.append(str_input[a:a+3])
        strlist.append(str_input[a+3:a+6])
    elif len_str>3:
        strlist.append(None)
        strlist.append(None)
        strlist.append(str_input[0:a])
        strlist.append(str_input[a:a+3])
    else:
        strlist.append(None)
        strlist.append(None)
        strlist.append(None)
        strlist.append(str_input[0:a])
    return strlist
def sanweishu(str_input):
    '''三位数的表示'''
    len_str=len(str_input)
    if len_str==3:
        ''''''
        n = int(str_input[2])
        a=int(str_input[0])
        b=int(str_input[1])
        if b==0:
            #return "{} Hundred {}".format(singles[str_input[0]-1],singles[str_input[2]-1])
            if a==0:
                return f"{singles[n - 1]}"
            else:
                return f"{singles[a - 1]} Hundred {singles[n - 1]}"
        elif b==1:
            if a==0:
                return f"{teens[n ]}"
            return f"{singles[a- 1]} Hundred {teens[n ]}"
        else:
            if a==0 and n==0:
                return f"{tens[b - 1]}"
            elif a==0:
                return f"{tens[b-1]} {singles[n - 1]}"
            elif n==0:
                return f"{singles[a- 1]} Hundred {tens[b-1]}"
            return f"{singles[a- 1]} Hundred {tens[b-1]} {singles[n - 1]}"
    elif len_str==2:
        ''''''
        n = int(str_input[1])#第二个
        b= int(str_input[0])#第一个
        # if n==0:
        #     #return "{} Hundred {}".format(singles[str_input[0]-1],singles[str_input[2]-1])
        #     return f"{singles[b - 1]}"
        if b==1:
            return f"{teens[n ]}"
        elif n==0:
            return f"{tens[b-1]}"
        else:
            return f"{tens[b-1]} {singles[n - 1]}"
    elif len_str==1:
        ''''''
        n = int(str_input[0])
        return f"{singles[n - 1]}"


singles = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
thousands = ["Thousand", "Million", "Billion"]

s_input=input("请输入一个整数:")
s=English_explanation(s_input,0)



'''456,123,456,789,123把整个字符串切分为每组12个字符 
32456123456789123
102005030780
'''
# group_num=math.ceil(len(s_input)/12)#表示group里面有几个元素
# a=len(s_input)%12
# group_num=[]
# if a!=12:
#     group=[s_input[0:a]]
# for i in range(0,group_num-1):
#     sub_s=s_input[a+i*12:a+i*12+12]
#     group.append(sub_s)
# # print(group)
# out_list=[]
# for i in range(len(group)):
#     num=len(group)-i-1
#     out_list.append(English_explanation(group[i],num))
#s=" ".join(out_list)
print(s)


'''下楼梯
def judge_single(num):
    if num%2!=0:
        return True
    else:
        return False
# def search_way_and_sum(begin,end):
#     if begin+1==end:
#         return 1,begin+end
#     if begin + 2 == end:
#         return 2,begin+end
#     return (search_way_and_sum(begin+1,end)[0]+search_way_and_sum(begin+2,end)[0],
#             begin+min(search_way_and_sum(begin+1,end)[1],search_way_and_sum(begin+2,end)[1]))
# a,b=map(int,input().split())
# num_way,min_sum=search_way_and_sum(a,b)
# print(num_way,min_sum)

a,b=map(int,input().split())
nums={}
minsum={}
for i in range(b-1,a-1,-1):
    if i==b-1:
        nums[i]=1
        minsum[i]=b+i
        continue
    if i==b-2:
        nums[i]=2
        minsum[i] = b + i
        continue
    nums[i]=nums[i+1]+nums[i+2]
    minsum[i]=min(i+minsum[i+1],i+minsum[i+2])
print(nums[a],minsum[a])
'''

'''3 20
2584 111'''
"""h指数"""
'''[0,1,2,4,3,5,8,3,6,8,9,4]
    [3,3,2,3,5,6,1325,4,31,21,4,5,3,1]
citations=eval(input("输入一个整数数组："))
cite_num=set(citations)
dict_cite_num={}#表示被引用次数对应的字典
for i in cite_num:
    dict_cite_num[i]=0
for i in citations:
    for j in dict_cite_num.keys():
        if i>=j:
            dict_cite_num[j]+=1
print(dict_cite_num)
probable_num=[]
for k,v in dict_cite_num.items():
    if k>=v:
        probable_num.append(v)
res=max(probable_num)
print(res)
'''



