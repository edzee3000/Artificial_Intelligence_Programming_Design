

#走楼梯问题
# def climbing_stairs(n:int):
#     """Write your code here"""
#     if n==1:
#         return 1
#     if n==2:
#         return 2
#     return climbing_stairs(n-1)+climbing_stairs(n-2)
# a,b=map(int,input())




# #求解所有子集
# from typing import List
# def subsets(nums: List[int]) -> List[List[int]]:
#     """
#     求子集
#     :param nums: List[int] 列表数据结构给定的数组
#     Return
#     List[List[int]] 返回所有的子集，每个子集组成一个列表，列表中每个元素为一个子集，子集中的元素为int类型
#     """
#     """ Write your code here"""
#     if len(nums)==0:
#         return [[]]
#     return [[nums[0]]+sub_list for sub_list in subsets(nums[1:])]+subsets(nums[1:])




# def swap_max_with_first_pure(nums):
#     """
#     纯函数版本：找出列表中最大的数，并将其与列表中第一个数的位置交换，返回一个新的列表
#     Args:
#     nums -- 输入的正整数组成的列表。
#     Returns:
#     一个新的列表，其中最大的数与第一个数交换了位置。
#     """
#     """Please write your code here"""
#     max_num=nums[0]
#     max_index=0
#     for i in range(len(nums)):
#         if nums[i]>=max_num:
#             max_num=nums[i]
#             max_index=i
#     nums_copy=nums.copy()
#     nums_copy[0],nums_copy[max_index]=nums_copy[max_index],nums_copy[0]
#     return nums_copy
#
#
# def swap_max_with_first_non_pure(nums):
#     """
#     非纯函数版本：找出列表中最大的数，并将其与列表中第一个数的位置交换，修改原列表。
#     Args:
#     nums -- 输入的正整数组成的列表。
#     无返回值，直接在原列表上进行修改。
#     """
#     """Please write your code here"""
#     max_num = nums[0]
#     max_index = 0
#     for i in range(len(nums)):
#         if nums[i] >= max_num:
#             max_num = nums[i]
#             max_index = i
#     nums[0], nums[max_index] = nums[max_index], nums[0]


# def my_pow(x: int, n: int):
#     """
#     幂计算
#     :param x: int 底数
#     :param n: int 幂
#     :return: int 结果
#     """
#     """ Write your code here"""
#     if n==0:
#         return 1
#     if n==1:
#         return x
#     if n==2:
#         return x*x
#     if n==3:
#         return x*x*x
#     return x*x*x*x*my_pow(x,n-4)




















