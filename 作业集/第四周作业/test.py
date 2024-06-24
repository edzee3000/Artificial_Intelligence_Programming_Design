#验证哥德巴赫猜想，输出10e9以内所有的偶数分解为两个质数的和

'''
def judge_sushu(num):
    for i in range(2,int(num**0.5+1)):
        if num%i==0:
            return False
    return True
sushu={2}
sushu_list=[2,3]
for i in range(5,int(10e5+1),2):
    if judge_sushu(i):
        sushu_list.append(i)
sushu=set(sushu_list)
print("4=2+2")
# for num in range(6,int(10e9+1),2):
#     judgesushu=False
#     for i in range(2,num):
#         if i not in sushu:
#             i_sushu=judge_sushu(i)
#             if not i_sushu:
#                 continue
#             else:
#                 sushu.add(i)
#         delta=num-i
#         if delta not in sushu:
#             judgesushu=judge_sushu(delta)
#             if judgesushu:
#                 sushu.add(delta)
#         else:
#             judgesushu=True
#         if judgesushu:
#             print(f"{num}={i}+{delta}")
#             break
#     if not judgesushu:
#         print(f"{num}不满足哥德巴赫猜想")
#         break
for num in range(6,int(10e9+1),2):
    judgesushu=False
    for i in sushu_list:
        if i not in sushu:
            i_sushu=judge_sushu(i)
            if not i_sushu:
                continue
            else:
                sushu.add(i)
                sushu_list.append(i)
        delta=num-i
        if delta not in sushu:
            judgesushu=judge_sushu(delta)
            if judgesushu:
                sushu.add(delta)
                sushu_list.append(i)
        else:
            judgesushu=True
        if judgesushu:
            print(f"{num}={i}+{delta}")
            break
    if not judgesushu:
        print(f"{num}不满足哥德巴赫猜想")
        break
'''


# #将str类型字符串转化为int类型的数组并升序排序
# def convert_str_to_sorted_list(s):
#     s = list(map(int, s.split(",")))
#     list(s).sort()
#     return s
# def check_minimum(nums):
#     nums = list(nums)
#     flag = True
#     for i in range(1, len(nums)):
#         flag = flag and nums[i] % nums[0] != 0
#     return flag
# def get_factors(num):
#     fac = []
#     for i in range(2, num):
#         if num % i == 0:
#             fac.append(i)
#             #fac.append(num, i)
#     list(set(fac)).sort()
#     ################这里出了问题应该是fac=list(set(fac)).sort()需要重新赋值给fac
#     return fac
# def get_gcd(factors, nums):
#     for fac in factors:
#         flag = True
#         for num in nums:
#             flag = flag and num % fac != 0
#         if flag:
#             return fac
#     return 1
# def main(input_text):
#     test_nums = input_text #传入一串"num1,num2,num3,……的字符串"
#     test_nums = convert_str_to_sorted_list(test_nums) #将字符串改为int类型升序排序的列表
#     if check_minimum(test_nums):
#         gcd = test_nums[0]
#     else:
#         factors = get_factors(test_nums[0])
#         gcd = get_gcd(factors, test_nums)
#     return str(gcd)
# import random
# import math
# def generator():
#     # 设置一个数组长度
#     array_length=100
#     # 从1开始从小到大循环生成数组中的每个元素
#     # 生成input_texts列表，以及对应的answers列表
#     input_texts: list = []
#     answers: list = []
#     # 在此处编写生成函数
#     #生成array_length个测试样例
#     for i in range(array_length):
#         """生成array_length个测试样例"""
#         #随机生成2~8个整数组成一个text列表
#         text=[random.randint(2,100) for j in range(random.randrange(2,9))]
#         answer_of_text=math.gcd(text[0],text[1])
#         for j in range(2,len(text)):
#             answer_of_text=math.gcd(text[j],answer_of_text)
#         text=[str(num) for num in text]
#         text=",".join(text)
#         input_texts.append(text)
#         answers.append(answer_of_text)
#     return input_texts, answers
# def test():
#     input_texts, answers = generator()
#     for input_text, ans in zip(input_texts, answers):
#         if main(input_text) != ans:
#             print(f"""
#                 发现错误用例：
#                 input: {input_text}
#                 output: {ans}
#             """)
#             #break
# if __name__ == "__main__":
#     # 实际提交
#     # print(main(input()))
#     # 测试
#     test()

''''''
# def convert_str_to_sorted_list(s):
#     s = list(map(int, s.split(",")))
#     s.sort()##################这里list(s)相当于对s强制类型转换后给一个新的对象，再sort不改变s
#     print("s的值为：",s)
#     return s
# def get_partial_arrays(nums):
#     nums = list(nums)
#     results = []
#     for i in range(0, len(nums), 2):
#         results.append(nums[i:i + 1])
#     print(results)
#     return results
# def get_results_from_arrays(pair_arrays):
#     ans = 0
#     for pair in pair_arrays:
#         ans += min(pair)#############为什么是min？？？
#     print("ans值为：",ans)
#     return ans
# def main(input_text):
#     test_nums = input_text
#     test_nums = convert_str_to_sorted_list(test_nums)
#     partial_arrays = get_partial_arrays(test_nums)
#     result = get_results_from_arrays(partial_arrays)
#     return str(result)
# import random
# def generator():
#     # 设置一个数组长度
#     array_length =2
#     # 从1开始从小到大循环生成数组中的每个元素
#     # 生成input_texts列表，以及对应的answers列表
#     input_texts: list = []
#     answers: list = []
#     # 在此处编写生成函数
#     for i in range(array_length):
#         num1=random.randint(4, 100)#要生成一个偶数
#         if num1%2!=0:
#             num1+=1
#         text=[random.randint(-100,200) for j in range(0,num1)]
#         text_copy=text.copy()
#         text.sort(reverse=False)#升序排列
#         answer=0
#         print(text)
#         for i in range(0,num1,2):#接下来计算answer并加入到answers里面去
#             answer+=text[i]
#         answers.append(str(answer))
#         text=[str(num) for num in text_copy]#将text里面所有元素转换成str类型
#         text=",".join(text)
#         input_texts.append(text)
#         print("answer值为：",answer)
#     return input_texts, answers
#
#
# def test():
#     input_texts, answers = generator()
#     for input_text, ans in zip(input_texts, answers):
#         if main(input_text) != ans:
#             print(f"""
#                 发现错误用例：
#                 input: {input_text}
#                 output: {ans}
#             """)
#         else:
#             print("样例通过")
#
#
# if __name__ == "__main__":
#     # 实际提交
#     # print(main(input()))
#     # 测试
#     test()



import random
def return_aroune_state(state):
    """返回上下左右的状态，最后返回一个状态列表 上下左右"""
    up_state=[[i[0],i[1],i[2]] for i in state]
    down_state=[[i[0],i[1],i[2]] for i in state]
    left_state=[[i[0],i[1],i[2]] for i in state]
    right_state=[[i[0],i[1],i[2]] for i in state]
    #接下来寻找None的位置
    None_row=0
    None_column=0
    for i in range(3):
        for j in range(3):
            if state[i][j]==None:
                None_row=i
                None_column=j
    #接下来分情况讨论向上移动，向下移动，向左移动，向右移动的状态
    #向上移动
    if None_row==2:#在第三行不能移动
        up_state=None
    else:
        up_state[None_row][None_column]= up_state[None_row+1][None_column]
        up_state[None_row+1][None_column]=None
    #向下移动
    if None_row==0:#在第一行不能移动
        down_state=None
    else:
        down_state[None_row][None_column]= down_state[None_row-1][None_column]
        down_state[None_row-1][None_column]=None
    #向左移动
    if None_column==2:#在第三列不能移动
        left_state=None
    else:
        left_state[None_row][None_column]= left_state[None_row][None_column+1]
        left_state[None_row][None_column+1]=None
    # 向右移动
    if None_column == 0:  # 在第一列不能移动
        right_state = None
    else:
        right_state[None_row][None_column] = right_state[None_row][None_column - 1]
        right_state[None_row][None_column - 1] = None

    return [up_state,down_state,left_state,right_state]
#设置一个概率值确定要不要遍历ta
def choose_or_not(state):
    similar_num=0
    for i in range(3):
        for j in range(3):
            if state[i][j]==last_state[i][j]:
                similar_num+=1
    possibility_rate=similar_num**0.5/3
    ran=random.random()
    if ran<=possibility_rate:
        return True
    else:
        return False

#暂定采用BFS广度优先搜索
init_state=[[3,7,5],
            [2,None,4],
            [1,6,8]]
# init_state=[[4,1,3],
#             [None,2,6],
#             [7,5,8]]
last_state=[[1,2,3],
            [4,5,6],
            [7,8,None]]
dict_state={}#每一个结点都会有一个上下左右的相邻状态
dict_corresponding_node={}
open_list=[]#等待被遍历的结点加入进open_set当中去
close_list=[]#已经遍历过的结点都会加入到结点当中去之后便不再遍历
open_list.append(init_state)
tuple_init_state=((i[0],i[1],i[2]) for i in init_state)
tuple_last_state=((i[0],i[1],i[2]) for i in last_state)
while last_state not in open_list:
    #遍历如今在open_set中的每一个状态
    # open_list_copy=[[[i[0][0],i[0][1],i[0][2]],
    #                  [i[1][0],i[1][1],i[1][2]],
    #                  [i[2][0],i[2][1],i[2][2]]] for i in open_list]
    open_list_copy = [i for i in open_list]
    for state in open_list:
        if not choose_or_not(state=state) and len(open_list)>=50:
            continue
        tuple_state=((i[0],i[1],i[2]) for i in state)
        dict_state[tuple_state] = return_aroune_state(state)#父节点指向四个子节点
        dict_corresponding_node[tuple_state]=state
        for i in range(len(dict_state[tuple_state])):
            if dict_state[tuple_state][i]==None:
                continue
            if (dict_state[tuple_state][i] in open_list
                    or dict_state[tuple_state][i] in close_list):#如果新状态已经在open_list当中了则将其归为None表示以后不会走这个点
                dict_state[tuple_state][i]=None
            elif (dict_state[tuple_state][i] not in open_list
                  and dict_state[tuple_state][i] not in close_list
                  and dict_state[tuple_state][i]!=None):
                open_list_copy.append(dict_state[tuple_state][i])
                print(dict_state[tuple_state][i])
        close_list.append(state)
        open_list_copy.remove(state)
    open_list=open_list_copy

print("该层循环结束")
#直到last_state在open_set里面即找到了这个点则寻找路径
path_list=[last_state]
print(dict_state.keys())
while init_state not in path_list:
    for key in dict_state.keys():
        list_key=[[i[0],i[1],i[2]] for i in dict_corresponding_node[key]]
        if path_list[0] in dict_state[key]:
            path_list.insert(0,list_key)
for i in path_list:
    print(i)



