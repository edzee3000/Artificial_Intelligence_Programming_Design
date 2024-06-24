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