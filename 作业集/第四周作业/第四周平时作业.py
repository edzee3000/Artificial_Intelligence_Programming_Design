'''
def solve(s):
    ans = None
    # write your code here
    # ********** Begin **********#
    ans=feibo(1,1,s,1)
    # **********  End  **********#
    return ans
def feibo(num1,num2,want,index):
    if num2==want:
        return index
    else:
        return feibo(num2,num1+num2,want,index+1)
def main():
    s = eval(input())
    print(solve(s))
if __name__ == "__main__":
    main()'''

"""
def solve(n):
    n=str(n)
    n=n.split()
    ans = None
    # write your code here
    # Below is one possible approach
    # ********** Begin **********#
    ans = 0
    for i in range(len(n)):
        n_copy=n.copy()
        
            
    # Fill the recursive structure

    # **********  End  **********#
    return ans

def generate_num(current_str,current_num):#传入
    ''''''
# def search_num(current_str_list,count):
#     if len(current_str_list)==1:
#         count+=1
#         return count
#     #current_str_list=current_str.split()
#     current_str_list_copy1=current_str_list.copy()
#     current_str_list_copy1.pop(0)#开始抛去第一个位置
#     current_str_list_copy2=current_str_list.copy()
#     for i in range(1,len(current_str_list_copy2)):
#         if current_str_list_copy2[i]<=current_str_list_copy2[0]:
#             current_str_list_copy3 = current_str_list_copy2.copy()
#             current_str_list_copy3[i],current_str_list_copy3[0]=current_str_list_copy3[0],current_str_list_copy3[i]
#             count=search_num(current_str_list_copy3,count)
#     count=search_num(current_str_list_copy1,count)
#     return count
def main():
    n = eval(input())#输入一个数字转换为str字符串
    print(solve(n))
if __name__ == "__main__":
    main()
"""

'''
def solve(n):
    ans = None
    # write your code here
    # Below is one possible approach
    # ********** Begin **********#
    ans = 0
    # Fill the recursive structure
    n=str(n)
    len_n=len(n)
    count=[0]
    dfs(0, "",list(n),count,len_n,n)
    ans=count[0]
    # **********  End  **********#
    return ans
def dfs(current_index, current_str,input_list,count,len_n,n):
    # Recursive end point determination
    if current_index==len_n and current_str<=n:
        count[0]+=1
        return
    for i in range(len(input_list)):
        input_list_copy=input_list.copy()
        input_list_copy.pop(i)
        dfs(current_index+1, current_str+input_list[i] ,input_list_copy,count,len_n,n)
def main():
    n = eval(input())
    print(solve(n))
if __name__ == "__main__":
    main()

'''
"147523"


'''
def solve(n):
    ans = None
    # write your code here
    # Below is one possible approach
    # ********** Begin **********#
    # Fill the recursive structure
    


    # **********  End  **********#
    return ans
def main():
    n = eval(input())
    print(solve(n))
if __name__ == "__main__":
    main()'''



'''
def solve(arr):
    ans = None
    # write your code here
    #********** Begin **********#
    sum=0
    for i in arr:
        sum+=i
    if sum%4!=0:
        return False
    sum=sum//4#每个部分的目标总和
    ans=if_sum_equal_target(arr,sum,1)
    #**********  End  **********#
    return ans
def if_sum_equal_target(arr,sum,num):
    arr_copy=arr.copy()
    sum_i=0
    for i in arr:
        sum_i+=i
        arr_copy.remove(i)
        if sum_i==sum:
            if arr_copy==[] and num==4:
                return True
            return if_sum_equal_target(arr_copy,sum,num+1)
        # elif sum_i>sum:
        #     return False
        else:
            continue
    return False

def main():
    arr = eval(input())
    print(solve(arr))
if __name__ == "__main__":
    main()
'''

'''
import re
def solve():
    ans = None
    # write your code here

    # Because the number of input key-value pairs will change according to n,
    # and the output value has multiple.
    # For convenience, this problem needs to handle its own input and output
    # ********** Begin **********#
    num=int(input())
    arr=[input() for i in range(num)]
    for i in range(len(arr)):#将arr分割为列表
        arr[i]=arr[i].split(":")
        arr[i][1]=arr[i][1].split("year")
        arr[i][1][1] = arr[i][1][1].split("month")
        arr[i][1].append(arr[i][1][1][0])
        arr[i][1].append(arr[i][1][1][1])
        arr[i][1].pop(1)
        arr[i][1][2] = arr[i][1][2].split("day")
        arr[i][1][2]= arr[i][1][2][0]
        for j in range(len(arr[i][1])):
            arr[i][1][j]=int(arr[i][1][j])
    dict_name_birth={}
    for i in arr:
        dict_name_birth[i[0]]=(i[1][0]-1)*365+month_to_day(i[1][1])+i[1][2]
    min_age=max(dict_name_birth.values())
    max_age=min(dict_name_birth.values())
    dict_name={}
    for key in dict_name_birth.keys():
        if dict_name_birth[key]==max_age:
            dict_name["old"]=key
        elif dict_name_birth[key]==min_age:
            dict_name["young"] = key
    print(arr)

    print(f"{dict_name['old']} {dict_name['young']}")
    print(dict_name_birth[dict_name['young']]-dict_name_birth[dict_name['old']])
    # **********  End  **********#
    return ans
def month_to_day(month):
    if month==1:
        return 0
    if month==2:
        return 31
    if month == 3:
        return 31+28
    if month == 4:
        return 31 + 28+31
    if month == 5:
        return 31 + 28 + 31+30
    if month == 6:
        return 31 + 28 + 31+30+31
    if month == 7:
        return 31 + 28 + 31+30+31+30
    if month == 8:
        return 31 + 28 + 31 + 30 + 31 + 30+31
    if month == 9:
        return 31 + 28 + 31 + 30 + 31 + 30 + 31+31
    if month == 10:
        return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31+30
    if month == 11:
        return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30+31
    if month == 12:
        return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31+30
def main():
    solve()
if __name__ == "__main__":
    main()'''




# #考虑采用深度优先搜索算法（递归深度太深了溢出了）
# class Node:
#     def __init__(self,state):
#         self.state=state
#     def around_state(self,state_list):
#         self.up_state=Node(state_list[0])
#         self.down_state = Node(state_list[1])
#         self.left_state=Node(state_list[2])
#         self.right_state = Node(state_list[3])
#
#
# def return_aroune_state(state):
#     """返回上下左右的状态，最后返回一个状态列表 上下左右"""
#     up_state = [[i[0], i[1], i[2]] for i in state]
#     down_state = [[i[0], i[1], i[2]] for i in state]
#     left_state = [[i[0], i[1], i[2]] for i in state]
#     right_state = [[i[0], i[1], i[2]] for i in state]
#     # 接下来寻找None的位置
#     None_row = 0
#     None_column = 0
#     for i in range(3):
#         for j in range(3):
#             if state[i][j] == None:
#                 None_row = i
#                 None_column = j
#     # 接下来分情况讨论向上移动，向下移动，向左移动，向右移动的状态
#     # 向上移动
#     if None_row == 2:  # 在第三行不能移动
#         up_state = None
#     else:
#         up_state[None_row][None_column] = up_state[None_row + 1][None_column]
#         up_state[None_row + 1][None_column] = None
#     # 向下移动
#     if None_row == 0:  # 在第一行不能移动
#         down_state = None
#     else:
#         down_state[None_row][None_column] = down_state[None_row - 1][None_column]
#         down_state[None_row - 1][None_column] = None
#     # 向左移动
#     if None_column == 2:  # 在第三列不能移动
#         left_state = None
#     else:
#         left_state[None_row][None_column] = left_state[None_row][None_column + 1]
#         left_state[None_row][None_column + 1] = None
#     # 向右移动
#     if None_column == 0:  # 在第一列不能移动
#         right_state = None
#     else:
#         right_state[None_row][None_column] = right_state[None_row][None_column - 1]
#         right_state[None_row][None_column - 1] = None
#     return [up_state, down_state, left_state, right_state]
# def return_tuple_state(state):
#     tuple_state=((i[0],i[1],i[2]) for i in state)
#     return tuple_state
#
# def DFS_search(parent_node):
#     tuple_parent_node=return_tuple_state(parent_node)
#     kid_nodes=dict_state[tuple_parent_node]=return_aroune_state(parent_node)
#     dict_corresponding_state[tuple_parent_node]=parent_node
#     close_list.append(parent_node)
#     for kid in kid_nodes:
#         if kid==last_state:
#             return
#         if kid not in close_list and kid!=None:
#             DFS_search(kid)
# init_state=[[1,2,3],
#             [4,None,6],
#             [7,5,8]]
# last_state=[[1,2,3],
#             [4,5,6],
#             [7,8,None]]
# dict_state={}#每一个结点都会有一个上下左右的相邻状态
# dict_corresponding_state={}
# open_list=[]#等待被遍历的结点加入进open_set当中去
# close_list=[]#已经遍历过的结点都会加入到结点当中去之后便不再遍历
# tuple_init_state=((i[0],i[1],i[2]) for i in init_state)
# tuple_last_state=((i[0],i[1],i[2]) for i in last_state)
# DFS_search(init_state)
# path_list=[last_state]
# print(dict_state.keys())
# while init_state not in path_list:
#     for key in dict_state.keys():
#         list_key=[[i[0],i[1],i[2]] for i in dict_corresponding_node[key]]
#         if path_list[0] in dict_state[key]:
#             path_list.insert(0,list_key)
# print(path_list)
#



# dict.setdefault(key, default=None)
