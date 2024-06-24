
# # 输入订单的数据示例，为字典类型
# Order_sample = {"is_VIP_customer": True, "cart" :{"Item1": 10, "Item2": 20, "Item3": 2}}
# def Decoration_func(func):
#     '''装饰器函数'''
#     def wrapper(*args,**kwargs):
#         ''''''
#         func_name=func.__name__
#         res=func(*args,**kwargs)
#         print(f'在优惠策略{func_name}下，优惠金额为{res}，该顾客是否为VIP：{kwargs["order"]["is_VIP_customer"]}')
#         return res
#     return wrapper
# #注意商品单价均为1
# @Decoration_func
# def fidelity_promo(order):
#     """为VIP顾客提供5%折扣"""
#     if order["is_VIP_customer"]:
#         return sum(order["cart"].values())*0.05
#     else:
#         return int(0)
# @Decoration_func
# def bulkitem_promo(order):
#     """单个商品为20个或以上时为该商品提供10%折扣"""
#     if sum(order["cart"].values())>=20:
#         return sum(order["cart"].values())*0.1
#     else:
#         return int(0)
# def best_promo(order,promos):
#     """选择可用的最佳折扣，并返回最大折扣"""
#     max_preferential=0
#     for func in promos:
#         if func(order=order)>max_preferential:
#             max_preferential=func(order=order)
#     return max_preferential
# @Decoration_func
# def large_order_promo(order):
#     """订单中的不同商品达到3个或以上时为多有商品提供7%折扣"""
#     if len(order["cart"].keys())>=3:
#         return sum(order["cart"].values()) * 0.07
#     else:
#         return int(0)
# promos = [fidelity_promo, bulkitem_promo]
# promos.append(large_order_promo)
# print(best_promo(Order_sample,promos=promos))




''''''
import time

''''''
# import time
# #输出被装饰函数的运行时间
# def Decoration_func(func):
#     '''装饰器函数'''
#     def wrapper(*args,**kwargs):
#         ''''''
#         time1=time.time()
#         res=func(*args,**kwargs)
#         time.sleep(0.0000001)
#         time2=time.time()
#         print(f"函数{func.__name__}运行所花的时间为：{time.time()-time1:.20f}秒")
#         return res
#     return wrapper
# @Decoration_func
# def add(a, b):
#     return a + b
# @Decoration_func
# def say_hello(name):
#     return f"Hello, {name}!", f"你好，{name}!"
# print(add(3,4))
# print(say_hello("edzee3000"))



import time
#通用的search框架
def search(Node,open_list,path,end_state,optimal_path,
           generate_kid_Node,judge_end_func,record_path_func,limit_depth=7,pruning_fuc=None):
    '''在通用的search框架中需要传入的参数为：
    变量：当前节点的对象、已经遍历过的结点列表、最大深度限制在默认30以内、目前最大的深度、最短路径
    函数：生成子节点的函数、剪枝函数、判断是否结束函数、记录路径函数、限制最大深度函数
    '''
    def renew_optimal_path(path,optimal_path):
        '''这里更新最短路径'''
        if optimal_path==[] or len(optimal_path)>len(path):
            return path.copy()
        else:
            return optimal_path
    print(Node.state)
    record_path_func(path, Node)  # 记录当前结点路径
    open_list_copy=open_list.copy()
    open_list.append(Node.state)  # 否则将其加入到open_list当中去
    if Node.depth > limit_depth:
        return optimal_path#如果当前结点的深度已经超出限制的最大深度了则返回
    if judge_end_func(Node,end_state):#判断是否结束了
        '''如果结束了则返回即可'''
        optimal_path=renew_optimal_path(path,optimal_path)
        print("")
        print("")
        return optimal_path#如果结束了则更新最短路径并返回
    if Node.state in open_list_copy:#如果存在比当前结点浅层的结点，则进行剪枝
        return optimal_path#这里剪枝就意味着直接返回即可
    generate_kid_Node(Node)#生成Node的所有子节点
    for node in Node.kid_nodes:
        '''遍历当前结点的所有子节点'''
        if node==None:
            continue
        search(node,open_list,path,end_state,optimal_path,
               generate_kid_Node,judge_end_func,record_path_func,limit_depth)
        path.pop()#每返回一次就把path最后一个状态pop一下
        open_list.pop()
    return optimal_path

def eight_puzzle_problem():
    class Node:
        def __init__(self,state):
            self.state=state
            self.kid_nodes=[None]*4#子节点分别为上下左右移动
    def eight_puzzle_generate_node(Node):
        '''8-puzzle问题生成结点'''
        def copy_state(state):
            row=len(state)
            column=len(state[0])
            state_copy=[[None]*column for i in range(row)]
            for i in range(row):
                for j in range(column):
                    state_copy[i][j]=state[i][j]

def honoi_freestyle_problem():
    '''汉诺塔搜索问题升级版  有A B C D四个塔 任意给定一个初始状态和一个结束状态 寻找之间的最短路径
    这里需要明确的是这里每个节点的状态为一个字典
    形如{"A":[7],"B":[6,5,4,3,2,1],"C":[9,8],"D":[]}
    每次移动的时候，子节点只可能有6种情况，并且还存在与parent_node相重合的情况，需要判断除去
    '''
    class Node:
        def __init__(self, state,parent_node,depth=0):
            self.state = state
            self.parent_node=parent_node
            self.kid_nodes = [None] * 6  # 最多有6个子节点（事实上其实只有5个）
            self.set_depth()
        def set_depth(self):
            if self.parent_node!=None:
                self.depth=self.parent_node.depth+1
            else:
                self.depth=0
    def hanoi_generate_node(node):
        ''''''
        def copy_dict(state):
            '''拷贝一个字典，且字典的value是一个列表'''
            new_dict={}
            for i in state.keys():
                value=state[i].copy()
                new_dict[i]=value
            return new_dict
        keys=node.state.keys()
        values=node.state.values()
        index=0
        for i in keys:
            for j in keys:
                move_pole=node.state[i]
                on_pole=node.state[j]
                if move_pole==[]:
                    continue
                if move_pole!=on_pole and (on_pole==[] or move_pole[len(move_pole)-1]<on_pole[len(on_pole)-1]):
                    #表示可以移动的情况，将move_pole最上面移动到on_pole上
                    new_state=copy_dict(state=node.state)
                    for k in new_state.keys():
                        if k==j:
                            new_state[k].append(move_pole[len(move_pole)-1])
                    new_state[i].pop()
                    if node.parent_node!=None and new_state!=node.parent_node.state:
                        node.kid_nodes[index]=Node(new_state,node)
                        index+=1
                    elif node.parent_node==None:
                        node.kid_nodes[index] = Node(new_state, node)
                        index += 1
    def hanoi_judge_end_func(node,end_state):
        if node.state==end_state:
            return True
        else:
            return False
    def hanoi_record_path_func(path,node):
        '''记录当前的路径'''
        path.append(node.state)
    def print_optimal_path(optimal_path):
        '''打印最优路径'''
        for i in optimal_path:
            print(i)
    init_state={"A":[9,8,7],"B":[6,5,4,3,2,1],"C":[],"D":[]}
    end_state={"A":[7],"B":[6,5,4,3,2,1],"C":[9,8],"D":[]}
    root=Node(init_state,parent_node=None)
    optimal_path=search(root,[],[],end_state,[],
           hanoi_generate_node,hanoi_judge_end_func,hanoi_record_path_func)
    print("")
    print_optimal_path(optimal_path)
    
    
honoi_freestyle_problem()