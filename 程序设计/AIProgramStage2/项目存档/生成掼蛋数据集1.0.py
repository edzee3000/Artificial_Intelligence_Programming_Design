'''
生成掼蛋数据集过程大致如下：
（1）创建两个类AI1与AI2并生成54张牌分别分给它们，
并且按照从左到右从大到小的顺序进行排序（写成类方法）
（2）通过类方法生成它们手上的状态列表
（3）人为设置Q的规则：
出了牌的个数*10+(27-手上已有牌数)**2
-少了顺子*10-少了三连对*3-少了三连对*5-少了三带二*1-少了炸弹*15
+(27-没出牌之前的个数)**0.5*20*1/0（最后输了还是赢了）
·最后发现真复杂算了，根据延时奖励，其实还是最终获胜与否占比最大，每一步Q值设定还是以最终胜利与否决定：
Q值=(27-目前所拥有的牌)*胜利与否（100 / 50）
存入csv的格式如下：我方的牌序列、对方的牌序列（从大到小27不足用0补全）、我方与对方牌序列根据键值对产生、Q值


困难之处：Q值设定很麻烦，如果需要产生数据去驱动的话，
需要预先产生Q值但是Q值的设定规则很麻烦，如何判断一个状态是好还是差？
如何判断出这牌是好牌还是烂牌？




另外对上一个阶段的改进就是，需要将两副扑克发给两个人27张牌，剩下还有54张牌就不管了
但是为了方便，这里仍然是明牌
'''





import numpy as np
import pandas as pd
import random
import collections

# 创建一个Hand类表示玩家/AI手上的一手牌
"""一手牌"""
class Hand:
    dict_ranks = {'大王': 17, '小王': 16, '2': 15, 'A': 14,
                  'K': 13, 'Q': 12, 'J': 11,
                  '10': 10, '9': 9, '8': 8, '7': 7,
                  '6': 6, '5': 5, '4': 4, '3': 3}
    dict_num_to_rank={17: '大王', 16: '小王', 15: '2', 14: 'A',
                  13:'K',  12:'Q', 11: 'J',
                  10: '10', 9: '9', 8: '8', 7: '7',
                  6: '6', 5:'5', 4: '4', 3: '3'}
    def __init__(self):
        self.cards = np.zeros(27,dtype=np.int32)
    def __init__(self, card_list):
        '''注意传进来的时候都是数字，规定之后内部存储一律按照数字，只有输出的时候才按照牌面输出'''
        self.cards = np.array(card_list)
        self.cards=np.sort(self.cards)[::-1]
        self.search_combination()
    def print_cards(self):
        '''打印牌名'''
        print("当前拥有的牌为：",np.array(list(map(self.dict_num_to_rank.get, self.cards))))
    def search_combination(self):
        '''寻找所有的牌组合并将其合成一个2维数组
        顺序为："单"、"双"、"三同张"、"顺子"、"三连对"、"三带二"、"三同连张"、"炸弹"'''
        def search_single():
            '''寻找单张'''
            a=np.unique(self.cards)[::-1]
            # print(a)
            self.combination.append(np.array([np.array([i]) for i in a]))
            # print(self.combination[0])
        def search_double():
            '''寻找对子'''
            # a=np.empty((1,2))
            self.combination.append(np.unique(np.array(
                [np.array(self.cards[i]).repeat(2)
             for i in range(1,len(self.cards))
             if self.cards[i-1]==self.cards[i]]),axis=0)[::-1])
        def search_treble():
            '''寻找三同张'''
            self.combination.append(np.unique(np.array(
                [np.array(self.cards[i]).repeat(3)
                 for i in range(2, len(self.cards))
                 if self.cards[i-2]==self.cards[i-1]==self.cards[i]]), axis=0)[::-1])
        def search_shunzi():
            '''寻找顺子'''
            a=np.unique(self.cards)[::-1]
            self.combination.append(np.unique(np.array(
                [np.array(a[i-4:i+1:1])
                 for i in range(4, len(a))
                 if a[i-4]-4 ==a[i-3]-3 ==a[i-2]-2
                 == a[i - 1]-1 == a[i]]), axis=0)[::-1])
        def search_sanliandui():
            '''寻找三连对'''
            a=self.combination[1]
            self.combination.append(np.unique(np.array(
                [np.array(a[i-2:i+1]).flatten()
                 for i in range(2, len(a))
                 if a[i-2][0]-2 == a[i-1][0]-1 == a[i][0]]), axis=0)[::-1])
        def search_sandaier():
            '''寻找三带二'''
            a=self.combination[2]
            b=self.combination[1]
            self.combination.append(np.unique(np.array(
                [np.append(i,j)
                 for i in a for j in b if i[0]!=j[0]]), axis=0)[::-1])
        def search_santonglianzhang():
            '''寻找三同连张'''
            a = self.combination[2]
            self.combination.append(np.unique(np.array(
                [np.array(a[i - 1:i + 1]).flatten()
                 for i in range(1, len(a))
                 if a[i - 1][0] - 1 == a[i][0]]), axis=0)[::-1])
        def search_bomb():
            '''寻找炸弹'''
            a=self.cards
            count = collections.Counter(a)
            self.combination.append(np.unique(np.array(
                [np.array([i]).repeat(4)
                 for i in count.keys() if count[i]>=4]), axis=0)[::-1])
        self.combination=[]#创建矩阵存储拥有的牌组合，并且永远都是从大到小排序
        search_single()
        search_double()
        search_treble()
        search_shunzi()
        search_sanliandui()
        search_sandaier()
        search_santonglianzhang()
        search_bomb()
        # print(self.combination)
    def del_cards(self,card):
        '''传入card为ndarray数组要从原先的cards中删去'''
        # self.cards = np.delete(self.cards, np.where(self.cards == card)[0])
        for i in card:
            # print("索引为：",np.where(self.cards==i)[0][0])
            # self.cards = np.delete(self.cards, np.where(self.cards==i)[0][0])
            for j in range(len(self.cards)):
                if self.cards[j]==i:
                    self.cards = np.delete(self.cards,j)
                    break
#创建一个玩家类，只需要有相应的牌权参数与牌参数即可
class Player:
    priority_weight=(15,20,25,45,35,20,25,5)
    def __init__(self,hand):
        ''''''
        self.hand=hand
        self.priority=False



def initiative():
    '''拥有牌权'''
    global last_play_card,AI1,AI2,data,round,Datas,flag,last_kind,fini,datas
    player=AI1 if AI1.priority==True else AI2
    another=AI2 if player==AI1 else AI1
    name="AI1" if AI1.priority==True else "AI2"
    # print("这是第", round, "回合")
    '''接下来随机按照概率随机抽取'''
    a=random.choices(player.hand.combination, weights=Player.priority_weight,k=1)[0]
    while not a.any():
        a = random.choices(player.hand.combination, weights=Player.priority_weight, k=1)[0]
    b = a[np.random.choice(a.shape[0], size=1, replace=False), :][0]
    last_play_card=b
    # data={"玩家":name, "我方牌序列":player.hand.cards, "对方牌序列":another.hand.cards,
    #     "回合数":round, "胜负":None, "Q值":None}
    data=[name,b,player.hand.cards,another.hand.cards,round,None,None]
    Datas.loc[len(Datas)]=data
    player.hand.del_cards(b)
    datas.append(data)
    # print(name,"选择出：",b)
    #结束出牌，善后工作
    round+=1
    player.priority=False
    another.priority=True
    for i in range(len(player.hand.combination)):
        # print(player.hand.combination[i])
        if np.array_equal(np.array(a),np.array(player.hand.combination[i])):
            last_kind=i
            break
def follow():
    global last_play_card,AI1,AI2,data,round,Datas,flag,last_kind,fini,datas
    # print("这是第",round,"回合")
    # print("上一个回合种类为：",last_kind)
    player = AI1 if AI1.priority == True else AI2
    another = AI2 if player == AI1 else AI1
    name = "AI1" if AI1.priority == True else "AI2"
    '''先判断有没有牌可以出'''
    # print(name,"对应是否有牌：",player.hand.combination[last_kind].any())
    if not player.hand.combination[last_kind].any() or \
        compare(player.hand.combination[last_kind],last_play_card,last_kind) \
        and not player.hand.combination[7].any():
        #没有对应值
        fini=True#没有牌可以出
        data = [name,"不出",player.hand.cards, another.hand.cards, round, None, None]
        Datas.loc[len(Datas)] = data
        datas.append(data)
        # print("这里因为没有牌对应的牌可以出")
        # print(name,"不出")
        # 结束出牌，善后工作
        round += 1
        player.priority = False
        another.priority = True
        return
    '''有0.1的概率直接不出，有0.2概率直接出炸'''
    pro=random.random()
    # print("概率为：",pro)
    if pro<0.1:
        fini = True  # 不出牌
        data = [name, "不出", player.hand.cards, another.hand.cards, round, None, None]
        Datas.loc[len(Datas)] = data
        datas.append(data)
        # print("这里因为pro<0.1因此不出")
        # print(name, "不出")
        # 结束出牌，善后工作
        round += 1
        player.priority = False
        another.priority = True
        return
    elif pro<0.3 and pro>=0.1 and player.hand.combination[7].any():
        a=player.hand.combination[7]
    else:
        '''接下来随机按照概率随机抽取'''
        a = player.hand.combination[last_kind]
    b = a[np.random.choice(a.shape[0], size=1, replace=False), :][0]
    # while not cmp_card(b,last_play_card,last_kind):
    #     b = a[np.random.choice(a.shape[0], size=1, replace=False), :][0]
    last_play_card = b
    # print(name,"选择出：",b)
    # data={"玩家":name, "我方牌序列":player.hand.cards, "对方牌序列":another.hand.cards,
    #     "回合数":round, "胜负":None, "Q值":None}
    data = [name,b, player.hand.cards, another.hand.cards, round, None, None]
    Datas.loc[len(Datas)] = data
    datas.append(data)
    player.hand.del_cards(b)
    # 结束出牌，善后工作
    round += 1
    player.priority = False
    another.priority = True
    fini = False
    for i in range(len(player.hand.combination)):
        # print(player.hand.combination[i])
        if np.array_equal(np.array(a),np.array(player.hand.combination[i])):
            last_kind=i
            break
def judge_finish():
    global last_play_card,AI1,AI2,data,round,Datas,flag,last_kind,fini,datas
    if len(AI1.hand.cards) == 0:
        flag =1
    elif len(AI2.hand.cards)==0:
        flag=2
    else:
        flag=0
def compare(combination,a2,last):
    '''有没有牌可以出'''
    '''"单"、"双"、"三同张"、"顺子"、"三连对"、"三带二"、"三同连张"、"炸弹"'''
    if last in range(5) or list in range(6,8):
        for i in combination:
            if i[0] >a2[0]:
                return True
    elif last==5:
        for i in combination:
            if i[0]>a2[0] or i[0]==a2[0] and i[3]>a2[3]:
                return True
    # print("返回False")
    return False
def cmp_card(a1,a2,last):
    # print("a1为",a1)
    if last!=7 and len(a1)==4:
        return True
    if (last in range(5) or last in range(6,8)) and a1[0] >a2[0]:
        return True
    elif last==5:
        if a1[0] > a2[0] or a1[0] == a2[0] and a1[3] > a2[3]:
            return True
    # print("返回False")
    return False

def process_Datas():
    global Datas,init_size,now_size,flag
    if now_size-init_size>=100:
        Datas=Datas.iloc[:init_size,:]
        return
    Datas.iloc[init_size:now_size :2, 5] = 1 if str(flag) in Datas.iloc[init_size,0] else 0
    Datas.iloc[init_size+1:now_size :2, 5] = 1 if str(flag) in Datas.iloc[init_size+1,0] else 0
    #Q值 = (27 - 目前所拥有的牌) * 胜利与否（100 / 50）
    for i in range(init_size, now_size):
        Datas.iloc[i, 6]=(27-len(Datas.iloc[i, 2]))*(Datas.iloc[i, 5]*50+50)


if __name__=="__main__":
    Datas=pd.DataFrame(columns=["玩家","出牌","我方牌序列","对方牌序列","回合数","胜负","Q值"])

    for n in range(5000):#生成5000份数据集
        init_size=len(Datas)
        data=[]
        datas=[]
        all_cards=np.append(np.arange(3,16,1).repeat(8),np.arange(16,18).repeat(2))
        np.random.shuffle(all_cards)
        all_cards=all_cards.reshape((4,27))
        AI1 = Player(Hand(all_cards[0]))  ########在这里AI1相当于之前写的main_player，AI2相当于之前的AI
        AI2 = Player(Hand(all_cards[1]))
        # print("AI1的牌库为：", AI1.hand.cards)
        # print("AI2的牌库为：", AI2.hand.cards)
        # 接下来确定牌权并清空上一轮出牌
        a=[True,False]
        random.shuffle(a)
        AI1.priority, AI2.priority=tuple(a)
        last_play_card=[]#对应的是值而不是名
        last_kind=None
        round=1#第一回合
        flag=0#1表示AI1赢，2表示AI2赢
        while flag==0:
            '''拥有牌权的AI先出，根据概率随机从牌序列当中选一个'''
            initiative()
            '''无牌权的AI决定是否跟牌'''
            fini=False
            while fini==False:
                follow()
                # print("fini的值为：",fini)
                # print("AI1当前牌序列为：", AI1.hand.cards)
                # print("AI2当前牌序列为：", AI2.hand.cards)
                judge_finish()
                if flag!=0:
                    break

            judge_finish()
        now_size=len(Datas)
        process_Datas()
        print("数据结果为：",Datas)

    print("数据结果为：",Datas)

Datas.to_csv(path_or_buf="掼蛋数据集")





'''
这个文件代码其实有很大的问题，就是在对战的时候生成数据集其实是有问题的，但是已经修改了好久好久了，真的改不动也改不会了，最后只能放弃了
'''