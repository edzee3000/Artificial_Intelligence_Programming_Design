#使用蒙特卡洛搜索树方法训练Agent下五子棋
#这里假定是人和Agent下棋，每下一次Agent就用一次蒙特卡洛搜素树去搜索找出最有可能赢的下法
import random
import math
def print_chequer(chequer):
    for i in chequer:
        print(i)
def judge_win_or_lose(chequer):
    '''用于判断游戏是否结束画出一个更大的棋盘
    如果游戏结束返回赢家的编号1或者2,1代表黑子，2代表白子'''
    '''判断是否有连续为1或2'''
    larger_chequer=[[0]*(size_of_chequer+4*2) for i in range(size_of_chequer+4*2)]
    for i in range(size_of_chequer):#复制中间一圈的值
        for j in range(size_of_chequer):
            larger_chequer[i+4][j+4]=chequer[i][j]
    for i in range(4,4+size_of_chequer):
        for j in range(4, 4 + size_of_chequer):
            if larger_chequer[i][j]==1 and search_continue_1_or_2(larger_chequer,i,j,1):
                return 1
            elif larger_chequer[i][j]==2 and search_continue_1_or_2(larger_chequer,i,j,2):
                return 2
    return 0
def search_continue_1_or_2(chequer,i,j,judge_num):
    #先判断左边连续5个，再判断右边连续5个，再判断上下，再判断对角线  如果有连续1返回1
    if chequer[i][j]==chequer[i][j-1]==chequer[i][j-2]==chequer[i][j-3]==chequer[i][j-4]==judge_num or \
            chequer[i][j] == chequer[i][j + 1] == chequer[i][j + 2] == chequer[i][j + 3] == chequer[i][j + 4] == judge_num or \
            chequer[i][j] == chequer[i-1][j] == chequer[i-2][j] == chequer[i-3][j] == chequer[i-4][j] == judge_num or \
            chequer[i][j] == chequer[i+1][j] == chequer[i+2][j] == chequer[i+3][j] == chequer[i+4][j] == judge_num or \
            chequer[i][j] == chequer[i-1][j-1] == chequer[i-2][j-2] == chequer[i-3][j-3] == chequer[i-4][j-4] == judge_num or \
            chequer[i][j] == chequer[i-1][j+1] == chequer[i-2][j+2] == chequer[i-3][j+3] == chequer[i-4][j+4] == judge_num or \
            chequer[i][j] == chequer[i+1][j-1] == chequer[i+2][j-2] == chequer[i+3][j-3] == chequer[i+4][j-4] == judge_num or \
            chequer[i][j] == chequer[i+1][j+1] == chequer[i+2][j+2] == chequer[i+3][j+3] == chequer[i+4][j+4] == judge_num :
        return judge_num
    return 0
def judge_allow_fall(chequer,row,column):
    if chequer[row-1][column-1]==0:
        return True
    else:
        return False
def copy_chequer(chequer):
    chequer_copy=[[0]*size_of_chequer for i in range(size_of_chequer)]
    for i in range(size_of_chequer):
        for j in range(size_of_chequer):
            chequer_copy[i][j]=chequer[i][j]
    return chequer_copy
def MonteCarloSearch(chequer):
    '''初始化第一个空节点'''
    root=Node(None,None)
    chequer_copy=copy_chequer(chequer)
    expand_parent_node(root=root,chequer=chequer_copy,player=1)
    for i in range(1,iteration+1):#迭代iteration次
        lowest_node=selection(root=root)
        win_or_lose=expand(parent_node=lowest_node)
        if win_or_lose:#如果是这个节点Agent赢了则反向传播
            ''''''
            BackPropagation_omega(win_or_lose, lowest_node)
            BackPropagation_UCB(lowest_node, i)
        else:#如果这个节点Agent还需要继续拓展
            #simulate_node=random.choice(random.choice(lowest_node.kid_node))#随机选取一个节点进行模拟  注意有2层
            win_or_lose=simulate(simulate_node=lowest_node)#模拟结果Agent是赢还是输
            BackPropagation_omega(win_or_lose,lowest_node)
            BackPropagation_UCB(lowest_node,i)
    print("所有子节点的UCB值为：")
    for line in root.kid_node:
        for node in line:
            if node !=None:
                print(node.UCB)
        print("")
    return search_max_probalility_state(root)
def expand_parent_node(root,chequer,player):
    '''初始化根节点的size_of_chequer*size_of_chequer个子节点'''
    for i in range(size_of_chequer):
        for j in range(size_of_chequer):
            if chequer[i][j]==0:
                chequer_copy=copy_chequer(chequer)
                chequer_copy[i][j]=player
                root.kid_node[i][j]=Node(state=chequer_copy,parent_node=root)#给子节点创建一个新的状态
            else:
                root.kid_node[i][j]=None
def selection(root):
    '''从root根节点开始选择寻找UCB最大的子节点'''
    move_node=root
    while not move_node.judge_kid_node():
        '''如果这个移动寻找的结点不是最后的结点'''
        move_node=move_node.search_UCB_max_node()#则寻找UCB最大的子节点
        move_node.n+=1
    #如果最后move_node是最后的结点则返回最后一个结点
    return move_node
def expand(parent_node):
    '''拓展部分，如果Agent没有胜利的话则继续拓展'''
    if parent_node.judge_Agent_win():
        '''Agent胜利的情况'''
        return True
    else:
        '''Agent还没有胜利'''
        expand_parent_node(root=parent_node,chequer=parent_node.state,player=2)
        return False
def simulate(simulate_node):
    '''随机选择了一个拓展后的结点进行模拟'''
    # for i in range(simulate_num):
    win_or_lose=RandomPolicy(simulate_node)#判断是否赢了
    if win_or_lose:
        return True
    else:
        return False
def RandomPolicy(simulate_node):
    '''采用随机策略进行模拟'''
    chequer_copy=copy_chequer(chequer=simulate_node.state)
    if random_fall(2,chequer_copy)==1:#Agent下完以后应当是另一个下了
        return True
    else:
        return False
def random_fall(player,chequer):
    '''玩家1和玩家2都随机落子，最终返回的是谁赢了，Agent赢返回1，'''
    another_player=3-player#player如果是1,another即为2
    chequer_copy = copy_chequer(chequer)
    print_chequer(chequer_copy)
    i=random.randint(0,size_of_chequer-1)
    j=random.randint(0,size_of_chequer-1)
    while chequer_copy[i][j]!=0:
        i = random.randint(0, size_of_chequer-1)
        j = random.randint(0, size_of_chequer-1)
    print("")
    chequer_copy[i][j]=player
    if judge_win_or_lose(chequer_copy)!=0:
        return judge_win_or_lose(chequer_copy)
    else:
        return random_fall(another_player, chequer_copy)
def BackPropagation_omega(win_or_lose,current_node):
    '''反向传播更新所有父节点的omega的值'''
    if current_node.parent_node==None:
        return
    if win_or_lose:
        current_node.omega+=1
        current_node.n+=1
    else:
        current_node.n+=1
    return BackPropagation_omega(win_or_lose,current_node.parent_node)
def BackPropagation_UCB(current_node,iteration):
    if current_node.parent_node==None:
        return
    if current_node.parent_node.parent_node==None:
        current_node.UCB=((current_node.omega/current_node.n)+
                          current_node.c*((math.log(iteration)/current_node.n)**0.5))
        return
    current_node.UCB = ((current_node.omega / current_node.n) +
                        current_node.c * ((math.log(current_node.parent_node.n) / current_node.n) ** 0.5))
    return BackPropagation_UCB(current_node.parent_node,iteration)
def search_max_probalility_state(root):
    max_node=None
    for line in root.kid_node:
        for node in line:
            if node!=None:
                max_node=node
    for line in root.kid_node:
        for node in line:
            if node!=None and node.UCB > max_node.UCB:
                max_node=node
    return max_node.state
class Node:
    def __init__(self,state,parent_node):
        '''每一个结点视为一个状态，下面有256中子节点'''
        self.state=state
        self.parent_node=parent_node
        self.kid_node=[[None]*size_of_chequer for i in range(size_of_chequer)]#注意这里是2层循环
        self.omega=0#omega表示该节点的胜利次数
        self.n=0#n表示该节点模拟次数/被访问次数
        self.c=2**0.5#c表示探索常数
        self.UCB=1000000000000#表示UCB是一个初始化很大的值
    def judge_kid_node(self):
        '''判断这个节点是否为最下面的节点'''
        for i in self.kid_node:
            for j in i:
                if j!=None:
                    return False
        return True
    def search_UCB_max_node(self):
        max_node=None
        for i in self.kid_node:
            flag=False
            for j in i:
                if j!=None:
                    max_node=j
                    flag=True
                    break
            if flag:
                break
        for i in self.kid_node:
            for j in i:
                if j!=None and j.UCB>max_node.UCB:
                    max_node=j
        return max_node
    def judge_Agent_win(self):
        larger_chequer = [[0] * (size_of_chequer + 4 * 2) for i in range(size_of_chequer + 4 * 2)]
        for i in range(size_of_chequer):  # 复制中间一圈的值
            for j in range(size_of_chequer):
                larger_chequer[i + 4][j + 4] = self.state[i][j]
        for i in range(4, 4 + size_of_chequer):
            for j in range(4, 4 + size_of_chequer):
                if larger_chequer[i][j] == 1 and search_continue_1_or_2(larger_chequer, i, j, 1):
                    return True
        return False


#初始化棋盘
size_of_chequer=11
iteration=300#迭代次数这里设定为300
#simulate_num=500#做出action之后需要进行模拟假设模拟500次
chequer=[[0]*size_of_chequer for i in range(size_of_chequer)]
#chequer[5][3]=chequer[5][4]=chequer[5][5]=chequer[5][6]=chequer[5][7]=2
#随机设定谁先手
initiative_right=1#1代表Agent先手，2代表玩家先手
random_rate=random.random()
if random_rate<0.5:#判断谁先手
    initiative_right=2
while(judge_win_or_lose(chequer=chequer)==0):
    ''''''
    if initiative_right==2:
        '''如果是玩家回合'''
        row,column=map(int,input("请输入你想落子的第几行第几列：").split())
        while(judge_allow_fall(chequer=chequer,row=row,column=column)==False):
            print("对不起您不允许在这个位置落子")
            row, column = map(int, input("请输入你想落子的第几行第几列：").split())
        chequer[row-1][column-1]=2
    else:
        '''如果是Agent回合接下来使用蒙特卡洛搜索树进行搜索'''
        chequer=MonteCarloSearch(chequer=chequer)
    print("当前棋局为：")
    print_chequer(chequer=chequer)
    initiative_right=3-initiative_right#更新回合
print_chequer(chequer)
print(judge_win_or_lose(chequer))






