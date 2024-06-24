

print("ok")



#sort函数
# from typing import List, Tuple
# import math
# def solve_mean(num_list):
#     sum_num=0
#     for i in range(len(num_list)):
#         sum_num+=num_list[i]
#     sum_num/=len(num_list)
#     return sum_num
# def solve_variance(num_list):
#     mean=solve_mean(num_list)
#     variance=0
#     for i in range(len(num_list)):
#         '''接下来求方差'''
#         variance+=(num_list[i]-mean)**2
#     variance/=len(num_list)
#     return variance
# def sort_test(nums: List[Tuple[int, int, int]]) -> (
#         Tuple)[List[Tuple[int, int, int]], List[Tuple[int, int, int]], List[Tuple[int, int, int]]]:
#     """
#     :param nums: List[Tuple[int, int, int]] 列表数据结构给定的数组
#
#     Return
#      Tuple[List[Tuple[int, int, int]], List[Tuple[int, int, int]], List[Tuple[int, int, int]]] 返回三种排序后的数组
#     """
#     """ Write your code here"""
#     num1, num2, num3 = None, None, None
#     num1=nums.copy()
#     num2=nums.copy()
#     num3 = nums.copy()
#     num1.sort(key=lambda x:max(x))#用lambda匿名函数传入判断函数
#     num2.sort(key=solve_mean)
#     num3.sort(key=solve_variance)
#     print(num1)
#     print(num2)
#     print(num3)
#     return num1, num2, num3
# sort_test([(3, -3, 6), (1, 1, 1), (2, 2, 2)])

#约瑟夫问题



'''
def round_leave(num: int, target: int):
    x = None
    have_leave=[False]*num
    point=0 #point=(point+1)%num
    while all_leave(have_leave)==False:
        current_num=0
        while current_num<target:
            if have_leave[point]==True:
                point=(point+1)%num
                continue
            current_num+=1
            if current_num==target:
                break
            point = (point + 1) % num
        have_leave[point]=True
        point = (point + 1) % num
    x=last_person(have_leave)
    return x
def all_leave(have_leave):
    num=0
    for i in have_leave:
        if i ==False:
            num+=1
    if num>=2:
        return False
    else:
        return True
def last_person(have_leave):
    for i in range(len(have_leave)):
        if have_leave[i] == False:
            return i
    return None
print(round_leave(7,4))'''


#判断特殊数
# from typing import List
# def judge_special_num(num):
#     str_num=str(num)
#     set_n_num=set({})
#     for i in range(1,len(str_num)+1):
#         set_n_num.add(i)
#     while num!=0:
#         i=num%10
#         num=num//10
#         if i not in set_n_num:
#             return False
#         set_n_num.remove(i)
#     return True
# def special_nums(nums: List[int]) -> List[int]:
#     """
#     :param nums: List[Tuple[int, int, int]] 列表数据结构给定的数组
#
#     Return
#      List[int] 只包含特殊数字的数组
#     """
#     """ Write your code here"""
#     results = None
#     results=[]
#     for num in nums:
#         '''遍历每一个数字判断其是否为特殊数'''
#         flag=judge_special_num(num)
#         if flag:
#             results.append(num)
#     return results
# if __name__ == "__main__":
#     nums = eval(input())
#     res = special_nums(nums)
#     print(res)


#买卖股票
# def maxProfit(prices):
#     max_profit = None
#     max_profit=0
#     for i in range(len(prices)-1):
#         for j in range(i+1,len(prices)):
#             '''第一次：i表示第几天买入，j表示第几天卖出'''
#             delta_price1= prices[j]-prices[i]
#             if delta_price1>=0:
#                 if delta_price1>max_profit:
#                     max_profit=delta_price1
#             else:
#                 continue
#             if j<= len(prices)-1-2:
#                 '''还能再买一次的情况'''
#                 for k in range(j+1,len(prices)-1):
#                     for l in range(k+1,len(prices)):
#                         '''若能再买一次的话'''
#                         delta_price2 = prices[l] - prices[k]
#                         if delta_price2 >= 0:
#                             sum_delta=delta_price1+delta_price2
#                             if sum_delta > max_profit:
#                                 max_profit = sum_delta
#     return max_profit
# if __name__ == "__main__":
#     prices = eval(input())
#     print(maxProfit(prices))




