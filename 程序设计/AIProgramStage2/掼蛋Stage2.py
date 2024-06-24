'''第二阶段主要完成的目标：
对于第一阶段的代码进行优化修改，对于接口的封装与面向对象编程的完善
对于掼蛋双人对战的要求更加严格，严格采用每人27张牌的形式去完成
主要采用深度学习的思想，对每一次action进行打分评价
主要采用神经网络回归模型预测方法
如果采用神经网络回归模型预测，如何用神经网络表示Q函数
（输入是状态和动作，然后输出一个标量，表示在状态下采取动作能获得的价值）
用txt文件记录其每一个玩家已经到了第几个回合了、出牌之前的状态、出完牌之后的状态、出什么牌、出完这个牌的Q值
并且对于最终的Q值应该综合：目前手中还有多少张牌、出手了多少张牌、能否出这个牌、出了这个牌会产生多少损失

接下来的计划：
（1）非可视化AI随机对战创建数据集（numpy和pandas）
（2）非可视化创建并训练模型（pytorch）
（3）可视化操作封装（pygame）
'''


import pygame
import random
import collections
import numpy as np
import pandas as pd
import torch

from NeuralNetwork import NetWork

#创建一个Card类表示一张牌
class Card:
    """一张牌"""
    RANKS = ['大王', '小王',
             '2', 'A', 'K', 'Q', 'J',
             '10', '9', '8', '7',
             '6', '5', '4', '3']
    dict_ranks={'大王':17, '小王':16, '2':15, 'A':14,
                'K':13, 'Q':12, 'J':11,
                '10':10, '9':9, '8':8, '7':7,
                '6':6, '5':5, '4':4, '3':3}
    dict_num_to_rank = {17: '大王', 16: '小王', 15: '2', 14: 'A',
                        13: 'K', 12: 'Q', 11: 'J',
                        10: '10', 9: '9', 8: '8', 7: '7',
                        6: '6', 5: '5', 4: '4', 3: '3'}
    SUITS = ['红桃', '方块', '黑桃', '梅花',"小王","大王"]
    dict_suits={'红桃':0, '方块':1, '黑桃':2, '梅花':3,"小王":4,"大王":5}
    pict_path=""
    def __init__(self, name, suit,face_up=True):
        self.name = name        # 牌面数字1~13以及大小王
        self.rank = Card.dict_ranks[name] # 牌对应大小
        self.suit = suit        # 花色
        self.is_face_up = face_up    # 是否显示牌的正面，True为正面，False为反面
        self.determine_path(name,suit)   #确定牌的路径
        self.card_name=self.determine_cardname()
        self.suit_num=self.dict_suits[suit]#花色对应的大小
        self.size=(size_of_screen_x/8,size_of_screen_y/4)
    def determine_path(self,rank, suit):
        if rank!="大王" and rank!="小王":
            self.pict_path=f"图片集\\{suit}{rank}.png"
        else:
            self.pict_path = f"图片集\\{rank}.png"
    def determine_cardname(self):
        if self.rank!="小王" and self.rank!="大王":
            return self.suit+str(self.rank)
        else:
            return self.rank
# 创建一个Hand类表示玩家/AI手上的一手牌
class Hand:
    """一手牌"""
    def __init__(self):
        self.cards = []       # cards列表变量存储牌手手里的牌
    def __init__(self, card_list):
        self.cards = card_list
        self.sort_hand_card()
        self.refresh_available_card_combination()
    def clear(self):         # 清空手里的牌
        self.cards = []
    def add(self, card):       # 增加手里的牌
        self.cards.append(card)
    def remove(self, card, other_hand):  # 减少手里的牌
        self.cards.remove(card)
    def print_all_card_name(self):
        for i in self.cards:
            print(i.card_name,end=" ")
        print("")
    def sort_hand_card(self):#按照顺序理牌
        for i in range(len(self.cards),1,-1):
            for j in range(0,i-1):
                if self.cards[j].rank < self.cards[j+1].rank:
                    self.cards[j],self.cards[j+1]=self.cards[j+1],self.cards[j]
                elif self.cards[j].rank == self.cards[j+1].rank:
                    if self.cards[j].suit_num<self.cards[j+1].suit_num:
                        self.cards[j], self.cards[j + 1] = self.cards[j + 1], self.cards[j]
    #接下来开始搜索出牌空间搜索出所有可能的动作        太麻烦了  于是最后改掉了 改成了对应的牌的点数组合
    def refresh_available_card_combination(self):
        '''将所有的出牌可能组合进一个字典当中，
        并规定字典的键为"单"、"双"、"三同张"、"顺子"、"三连对"、"三带二"、"三同连张"、"炸弹"'''
        self.card_combination = {}
        self.card_combination["单张"]=self.search_single()#这里是rank面额 而不是对应的点数大小
        self.card_combination["对子"]=self.search_double()
        self.card_combination["三同张"] = self.search_treble()  # 如果不存在返回为空列表即可
        self.card_combination["顺子"] = self.search_shunzi()
        self.card_combination["三连对"]=self.search_sanliandui()
        self.card_combination["三带二"] = self.search_sandaier()
        self.card_combination["三同连张"] = self.santonglianzhang()
        self.card_combination["炸弹"] = self.bomb()
        print(self.card_combination)
    def search_single(self):
        all_kind = list({card.rank for card in self.cards})
        all_kind= [[card] for card in all_kind]
        # all_kind=[return_str_of_numvalue(self.cards[0].dict_ranks,num) for num in all_kind]
        # print("单张组合有：",all_kind)
        return all_kind
    def search_double(self):
        double = []
        have_over_num=set({})
        for i in range(len(self.cards)-1,0,-1):
            if self.cards[i].rank == self.cards[i - 1].rank and self.cards[i].rank not in have_over_num:
                double.append([self.cards[i].rank,self.cards[i].rank])  # 注意这里可能会有重复 比如 222会拆成2|22 22|2
            have_over_num.add(self.cards[i].rank)
        # print("对子组合有：",double)
        return double
    def search_treble(self):
        treble = []
        have_over_num = set({})
        for i in range(len(self.cards) - 1, 1, -1):
            if (self.cards[i].rank == self.cards[i - 1].rank== self.cards[i - 2].rank and \
                    self.cards[i].rank not in have_over_num):
                treble.append([self.cards[i].rank]*3)  # 注意这里可能会有重复 比如 222会拆成2|22 22|2
            have_over_num.add(self.cards[i].rank)
        # print("三同张组合有：",treble)
        return treble
    def search_shunzi(self):
        shunzi=[]
        all_kind = list({card.rank for card in self.cards})
        all_kin_str=self.card_combination["单张"]
        for i in range(len(all_kind)-4):
            if all_kind[i]==all_kind[i+1]-1==all_kind[i+2]-2==all_kind[i+3]-3==all_kind[i+4]-4:
                shunzi.append([all_kin_str[i][0],all_kin_str[i+1][0],all_kin_str[i+2][0],all_kin_str[i+3][0],all_kin_str[i+4][0]])
        # print("顺子组合有：",shunzi)
        return shunzi
    def search_sanliandui(self):
        sanliandui=[]
        double=self.card_combination["对子"]
        # double_kind=[self.cards[0].dict_ranks[i[0]] for i in double]
        # double_kind_str=[i[0] for i in double]
        double_kind = [i[0] for i in double]
        for i in range(len(double_kind)-2):
            if double_kind[i]==double_kind[i+1]-1==double_kind[i+2]-2:
                sanliandui.append([double_kind[i]]*2+[double_kind[i+1]]*2+[double_kind[i+2]]*2)
        # print("三连对组合有：",sanliandui)
        return sanliandui
    def search_sandaier(self):
        sandaier=[]
        double=self.card_combination["对子"]
        treble=self.card_combination["三同张"]
        for i in treble:
            for j in double:
                if i[0]==j[0]:#排除有炸弹的时候炸弹既可以拆成三同张也可以拆为对子
                    continue
                sandaier.append(i+j)
        # print("三带二组合有：",sandaier)
        return sandaier
    def santonglianzhang(self):
        santonglianzhang = []
        treble = self.card_combination["三同张"]
        treble_kind = [i[0] for i in treble]
        for i in range(len(treble_kind) - 1):
            if treble_kind[i] == treble_kind[i + 1] - 1 :
                santonglianzhang.append(
                    [treble_kind[i]] * 3 + [treble_kind[i + 1]] * 3)
        # print("三同连张组合有：", santonglianzhang)
        return santonglianzhang
    def bomb(self):
        '''这里炸弹会有6种可能'''
        zhadan = []
        a=[]
        have_over_num = set({})
        for i in range(len(self.cards) - 1, 3, -1):
            if self.cards[i].rank == self.cards[i - 1].rank==self.cards[i-2].rank == self.cards[i - 3].rank \
                    and self.cards[i].rank not in have_over_num:
                a.append([self.cards[i].rank]*4)  # 注意这里可能会有重复 比如 222会拆成2|22 22|2
            have_over_num.add(self.cards[i].rank)
        zhadan+=a
        a=[]
        have_over_num = set({})
        for i in range(len(self.cards) - 1, 4, -1):
            if (self.cards[i].rank == self.cards[i - 1].rank
                    ==self.cards[i-2].rank == self.cards[i - 3].rank ==self.cards[i-4].rank\
                    and self.cards[i].rank not in have_over_num):
                a.append([self.cards[i].rank]*5)  # 注意这里可能会有重复 比如 222会拆成2|22 22|2
            have_over_num.add(self.cards[i].rank)
        zhadan+=a
        a = []
        have_over_num = set({})
        for i in range(len(self.cards) - 1, 5, -1):
            if (self.cards[i].rank == self.cards[i - 1].rank == self.cards[i - 2].rank
                    == self.cards[i - 3].rank == self.cards[i - 4].rank== self.cards[i - 5].rank\
                    and self.cards[i].rank not in have_over_num):
                a.append([self.cards[i].rank] * 6)  # 注意这里可能会有重复 比如 222会拆成2|22 22|2
            have_over_num.add(self.cards[i].rank)
        zhadan+=a
        a = []
        have_over_num = set({})
        for i in range(len(self.cards) - 1, 6, -1):
            if (self.cards[i].rank == self.cards[i - 1].rank == self.cards[i - 2].rank
                    == self.cards[i - 3].rank == self.cards[i - 4].rank == self.cards[i - 5].rank
                    == self.cards[i - 6].rank \
                    and self.cards[i].rank not in have_over_num):
                a.append([self.cards[i].rank] * 7)  # 注意这里可能会有重复 比如 222会拆成2|22 22|2
            have_over_num.add(self.cards[i].rank)
        zhadan+=a
        a = []
        have_over_num = set({})
        for i in range(len(self.cards) - 1, 7, -1):
            if (self.cards[i].rank == self.cards[i - 1].rank == self.cards[i - 2].rank
                    == self.cards[i - 3].rank == self.cards[i - 4].rank == self.cards[i - 5].rank
                    == self.cards[i - 6].rank == self.cards[i - 7].rank\
                    and self.cards[i].rank not in have_over_num):
                a.append([self.cards[i].rank] * 8)  # 注意这里可能会有重复 比如 222会拆成2|22 22|2
            have_over_num.add(self.cards[i].rank)
        zhadan+=a
        a = []
        for i in range(0,len(self.cards)-3):
            if self.cards[i].rank == self.cards[i - 1].rank ==17 and \
                self.cards[i - 2].rank == self.cards[i - 3].rank==16:
                a=[17,17,16,16]
        zhadan+=a
        # print("炸弹有：", zhadan)
        return zhadan
class AllCards:
    '''一整副牌'''
    RANKS = ['2', 'A', 'K', 'Q', 'J',
             '10', '9', '8', '7',
             '6', '5', '4', '3']
    SUITS = ['红桃', '方块', '黑桃', '梅花']
    def __init__(self):
        self.cards_list = []
        self.init_all_cards()
    def init_all_cards(self):
        for rank in reversed(self.RANKS):
            self.cards_list.append([Card(rank,suit) for suit in self.SUITS])
        self.cards_list.append([Card("小王","小王"),Card("大王","大王")])
        self.cards_list=[card for i in self.cards_list for card in i]
        random.shuffle(self.cards_list)
class Player:
    def __init__(self,url_img,loc):#确定玩家头像图片
        self.url_img=url_img
        self.location=loc
        self.cards_location_list=[]
        self.cards_pre_location_list=[]
        self.if_pre_play=[]#一个True/False的列表表示判断里面的牌是否准备出
        self.have_card_num=27#目前手中拥有牌的个数
        self.hand_card_list=None
        self.hand_card_num_value_list=None
        self.initiative=False #是否处于起牌状态
        self.following=False  #是否处于跟牌状态
    def set_hand_card_list(self,hand_list):
        self.hand_card_list=hand_list
        self.hand_card_num_value_list=[card.rank for card in hand_list.cards]
        self.hand_card_num_value_list.sort(reverse=True)
    def set_size(self,size):
        self.size=size
    def determine_first_card_location(self,first_location):
        '''确定玩家的第一张牌的位置 然后确定一个玩家所有牌位置的列表'''
        for i in range(self.have_card_num):
            self.cards_location_list.append([first_location[0]+i*delta_card , first_location[1]])
            self.cards_pre_location_list.append([first_location[0]+i*delta_card , first_location[1]-30])
            self.if_pre_play.append(False)
    def draw_all_card(self,screen):
        for i in range(len(self.hand_card_list.cards)):
            url_card=self.hand_card_list.cards[i].pict_path
            size = self.hand_card_list.cards[i].size
            card_img=pygame.image.load(url_card).convert()
            card_img= pygame.transform.scale(card_img, size)
            if self.if_pre_play[i]==False:
                card_loc=self.cards_location_list[i]
                screen.blit(card_img, card_loc)
            else:
                card_loc = self.cards_pre_location_list[i]
                screen.blit(card_img, card_loc)
                # print(url_card)
                # print(card_img)
                # print(card_loc)
    def judge_pre_play_card_kind(self):
        '''0代表不符合出牌要求，1代表单张，2代表对子，3代表三同张，4代表顺子，5代表三连对，
        6代表三带二，7代表三同连张，8代表炸弹'''
        '''规定主动出牌规则：先对牌进行搜索  '''
        '''规定跟牌规则：如果能跟则跟'''
        pre_play_list=[]#列表加入即将出牌的对象
        for i in range(len(self.hand_card_list.cards)):
            '''用pre_play去判断'''
            if self.if_pre_play[i]==True:
                pre_play_list.append(self.hand_card_list.cards[i])
        pre_play_numvalue_list=[card.rank for card in pre_play_list]
        #print(pre_play_numvalue_list)
        self.pre_play_list=pre_play_list
        #pre_play_numvalue_list.sort(reverse=False)
        print(pre_play_numvalue_list)
        try:
            if len(pre_play_numvalue_list)==1:
                return 1,pre_play_list#1代表单张
            elif len(pre_play_numvalue_list)==2 and \
                    pre_play_numvalue_list[0]==pre_play_numvalue_list[1]:
                return 2,pre_play_list#2代表对子
            elif len(pre_play_numvalue_list)==3 and \
                    pre_play_numvalue_list[0]==pre_play_numvalue_list[1]==pre_play_numvalue_list[2]:
                return 3,pre_play_list#3代表三同张
            elif len(pre_play_numvalue_list)==5 and \
                    pre_play_numvalue_list[0]==pre_play_numvalue_list[1]+1== \
                    pre_play_numvalue_list[2]+2== \
                    pre_play_numvalue_list[3]+3==pre_play_numvalue_list[4]+4:
                return 4,pre_play_list#4代表顺子
            elif len(pre_play_numvalue_list)==6 and \
                    pre_play_numvalue_list[0] == pre_play_numvalue_list[1] == \
                    pre_play_numvalue_list[2] + 1 == \
                    pre_play_numvalue_list[3] + 1 == pre_play_numvalue_list[4] + 2 == \
                    pre_play_numvalue_list[5] + 2:
                return 5,pre_play_list#5代表三连对
            elif len(pre_play_numvalue_list)==5 and \
                    ((pre_play_numvalue_list[0]==pre_play_numvalue_list[1] and pre_play_numvalue_list[2]== \
                    pre_play_numvalue_list[3]==pre_play_numvalue_list[4]  or  pre_play_numvalue_list[0]== \
                     pre_play_numvalue_list[1] == pre_play_numvalue_list[2] and \
                    pre_play_numvalue_list[3]==pre_play_numvalue_list[4] )) \
                    and pre_play_numvalue_list[0] != pre_play_numvalue_list[4]:
                return 6,pre_play_list#6代表三带二并且不是炸弹
            elif len(pre_play_numvalue_list)==6 and \
                    pre_play_numvalue_list[0] == pre_play_numvalue_list[1] == \
                    pre_play_numvalue_list[2]== \
                    pre_play_numvalue_list[3] + 1 == pre_play_numvalue_list[4] + 1 == \
                    pre_play_numvalue_list[5] + 1:
                return 7,pre_play_list#7代表三同连张
            elif (len(pre_play_numvalue_list)==4 and \
                    pre_play_numvalue_list[0] == pre_play_numvalue_list[1] == \
                    pre_play_numvalue_list[2] == pre_play_numvalue_list[3]) or \
                    (len(pre_play_numvalue_list) == 5 and \
                     pre_play_numvalue_list[0] == pre_play_numvalue_list[1] == \
                     pre_play_numvalue_list[2] == pre_play_numvalue_list[3]== pre_play_numvalue_list[4]) or \
                    (len(pre_play_numvalue_list) == 6 and \
                     pre_play_numvalue_list[0] == pre_play_numvalue_list[1] == \
                     pre_play_numvalue_list[2] == pre_play_numvalue_list[3] == \
                     pre_play_numvalue_list[4] == pre_play_numvalue_list[5]) or \
                    (len(pre_play_numvalue_list) == 7 and \
                     pre_play_numvalue_list[0] == pre_play_numvalue_list[1] == \
                     pre_play_numvalue_list[2] == pre_play_numvalue_list[3] == \
                     pre_play_numvalue_list[4] == pre_play_numvalue_list[5]== pre_play_numvalue_list[6]) or \
                    (len(pre_play_numvalue_list) == 8 and \
                     pre_play_numvalue_list[0] == pre_play_numvalue_list[1] == \
                     pre_play_numvalue_list[2] == pre_play_numvalue_list[3] == \
                     pre_play_numvalue_list[4] == pre_play_numvalue_list[5] == \
                     pre_play_numvalue_list[6] == pre_play_numvalue_list[7]) or \
                    (len(pre_play_numvalue_list) == 4 and \
                     pre_play_numvalue_list[0] == pre_play_numvalue_list[1]==17 and \
                     pre_play_numvalue_list[2] == pre_play_numvalue_list[3]==16):
                return 8,pre_play_list#8代表炸弹
            else:
                return 0,pre_play_list#0代表不符合出牌要求
        except:#0代表不符合出牌要求
            return 0,pre_play_list
class Button:
    def __init__(self, url_img):
        self.url_img=url_img
    def set_attribute(self,loc,size):
        self.loc = loc
        self.size = size
    def draw_button_image(self,screen):
        img = pygame.image.load(self.url_img).convert()
        img = pygame.transform.scale(img, self.size)
        screen.blit(img, self.loc)




'''有一个非常核心的函数就是已知需要出一副牌，需要通过ndarray数组来从手牌当中找出对应的牌并且打出'''
def draw_basic_background(screen,main_player,AI):
    url_background="图片集\牌桌.jpg"
    url_steve="图片集\史蒂夫.jpg"
    ulr_kulouma="图片集\骷髅马.jpg"
    #背景图
    background_img=pygame.image.load(url_background).convert()
    background_img = pygame.transform.scale(background_img, (size_of_screen_x, size_of_screen_y))
    #玩家图
    Steve_img=pygame.image.load(url_steve).convert()
    Steve_size=main_player.size
    Steve_img=pygame.transform.scale(Steve_img,Steve_size)
    #AI图
    kulouma_img=pygame.image.load(ulr_kulouma).convert()
    kulouma_size =AI.size
    kulouma_img = pygame.transform.scale(kulouma_img, kulouma_size)
    screen.blit(background_img,(0,0))
    screen.blit(Steve_img,(0,size_of_screen_y-Steve_size[1]))
    screen.blit(kulouma_img, (0, 0))
    #画按钮图
    button_locx=main_player.cards_location_list[26][0]+size_of_screen_x/8
    width = size_of_screen_x-button_locx
    button_locy_0=main_player.cards_location_list[26][1]-45
    height = (size_of_screen_y -button_locy_0)/4
    button_locy_1=button_locy_0+height
    button_locy_2=button_locy_1+height
    button_locy_3=button_locy_2+height
    reset_button.set_attribute(loc=(button_locx, button_locy_0),size=(width,height))
    play_button.set_attribute(loc=(button_locx, button_locy_1),size=(width,height))
    giveup_button.set_attribute(loc=(button_locx, button_locy_2), size=(width, height))
    suggestion_button.set_attribute(loc=(button_locx, button_locy_3), size=(width, height))
    reset_button.draw_button_image(screen=screen)
    play_button.draw_button_image(screen=screen)
    giveup_button.draw_button_image(screen=screen)
    suggestion_button.draw_button_image(screen=screen)
    #画玩家和AI的牌的图
    main_player.draw_all_card(screen=screen)
    AI.draw_all_card(screen=screen)
    #画已经被打出的牌
    if last_play_card !=[]:
        display_have_played_card(last_play_card)
def determine_priority(AI):#初始化确定谁先拥有牌权
    points=[card.rank for card in AI.hand_card_list.cards]
    if 17 in points:
        return False
    else:
        return True
def judge_mouse_event(main_player,mouse_loc):
    '''判断鼠标摁下去的行为'''
    remain_card_num=main_player.have_card_num=len(main_player.hand_card_list.cards)
    card_size=main_player.hand_card_list.cards[0].size
    if mouse_loc[0]<=main_player.cards_location_list[remain_card_num-1][0]+card_size[0] and \
        mouse_loc[0]>=main_player.cards_location_list[0][0] and \
        mouse_loc[1]<=size_of_screen_y and mouse_loc[1]>=main_player.cards_location_list[0][1]:
        pre_play_card(main_player,mouse_loc)
    elif mouse_loc[0]<=size_of_screen_x and mouse_loc[0]>=reset_button.loc[0] and \
        mouse_loc[1] <=size_of_screen_y and mouse_loc[1]>=reset_button.loc[1]:
        click_button(main_player, mouse_loc)
def pre_play_card(main_player,mouse_loc):#注意只有main_player才存在预出牌
    '''将牌点起来与放下去'''
    begin_x=main_player.cards_location_list[0][0]
    remain_card_num = main_player.have_card_num = len(main_player.hand_card_list.cards)
    index_of_card=min( int(mouse_loc[0]-begin_x)//int(delta_card) , remain_card_num-1)#求出摁到了第几张牌
    main_player.if_pre_play[index_of_card] = not main_player.if_pre_play[index_of_card]
    print(main_player.if_pre_play[index_of_card])
def click_button(main_player,mouse_loc):
    '''点击到了按钮区域'''
    '''如果摁到了出牌键但是也要考虑能不能出牌以及是否有牌要出'''
    loc_x=mouse_loc[0]
    loc_y=mouse_loc[1]
    #print(reset_button.loc[0],reset_button.loc[1])
    if loc_x>=reset_button.loc[0] and loc_x<=size_of_screen_x and \
            loc_y>=reset_button.loc[1] and loc_y<=reset_button.loc[1]+reset_button.size[1]:
        click_reset_button()#一键清空重置
    elif loc_x>=suggestion_button.loc[0] and loc_x<=size_of_screen_x and \
            loc_y>=suggestion_button.loc[1] and loc_y<=suggestion_button.loc[1]+suggestion_button.size[1]:
        '''执行建议命令根据当前状态给予建议'''
        click_suggest_button()
    elif loc_x>=giveup_button.loc[0] and loc_x<=size_of_screen_x and \
            loc_y>=giveup_button.loc[1] and loc_y<=giveup_button.loc[1]+giveup_button.size[1]:
        '''执行放弃指令'''
        click_giveup_button()
    elif loc_x>=play_button.loc[0] and loc_x<=size_of_screen_x and \
            loc_y>=play_button.loc[1] and loc_y<=play_button.loc[1]+play_button.size[1]:
        '''执行出牌指令'''
        click_play_button()
def return_point_corresponding_card(hand,num_value):#返回点大小的所有的牌对象比如15返回所有2,16返回小王
    card_list=[]
    for i in hand.cards:
        if i.dict_ranks[i.rank]==num_value:
            card_list.append(i)
    return card_list
def return_str_of_numvalue(dict_ranks,num):#返回numvalue值对应的键大小
    for key in dict_ranks.keys():
        if dict_ranks[key]==num:
            return key

def main_player_initiative():
    mouse_presses = pygame.mouse.get_pressed()
    if mouse_presses[0]:
        print("Left Mouse key was clicked")
        print(pygame.mouse.get_pos())
        mouse_loc = pygame.mouse.get_pos()
        judge_mouse_event(main_player, mouse_loc)
        main_player.hand_card_list.refresh_available_card_combination()
        #print(main_player.judge_pre_play_card_kind())
        draw_basic_background(screen=screen, main_player=main_player, AI=AI)
def AI_initiative():
    '''这里是AI起牌阶段'''
    AI.hand_card_list.refresh_available_card_combination()
    AI_play_card_initiative_rules()#最后返回要打的rank列表
def main_player_following():
    mouse_presses = pygame.mouse.get_pressed()
    if mouse_presses[0]:
        print("Left Mouse key was clicked")
        print(pygame.mouse.get_pos())
        mouse_loc = pygame.mouse.get_pos()
        judge_mouse_event(main_player, mouse_loc)
        main_player.hand_card_list.refresh_available_card_combination()
        draw_basic_background(screen=screen, main_player=main_player, AI=AI)
def AI_following():
    '''这里是AI跟牌阶段'''
    AI.hand_card_list.refresh_available_card_combination()
    AI_play_card_following_rules()  # 最后返回要打的rank列表



def click_reset_button():#如果按到了重置按钮
    for i in range(27):
        main_player.if_pre_play[i]=False
    print("摁下RESET键")
def click_giveup_button():
    #注意这里只有main_player才会选择放弃
    if main_player.initiative==True:
        display_word("Must Play Card Now")
        pygame.time.delay(1000)
        return
    for i in range(27):
        main_player.if_pre_play[i]=False
    main_player_not_following_card()
def click_play_button():
    kind,pre_play_list=main_player.judge_pre_play_card_kind()
    print("出牌种类为：",kind)
    pre_play_numvalue_list = [card.rank for card in pre_play_list]
    if kind==0:
        display_word("These Cards Not Allowed")
        pygame.time.delay(1000)
        return
    print("上家出的牌为：",last_play_numvalue_card)
    last_kind = judge_card_kind(last_play_numvalue_card)
    print("上家出的牌种类为：",last_kind)
    ##如果是在主玩家起牌阶段
    if main_player.initiative==True:
        '''接下来写出牌的部分'''
        play_card_list(main_player)
        last_play_card.clear()
        for card in main_player.pre_play_list:
            last_play_card.append(card)
        main_player_following_card()#表明接下来应该是AI的跟牌阶段
        return
    # 如果在主玩家跟牌阶段
    if main_player.following==True:
        '''先判断能不能出，是否比AI大，如果大则出，如果小则显示比AI小'''
        if kind==8:#8代表炸弹
            if kind!=last_kind:#上家非炸下家为炸
                play_card_list(main_player)
                main_player_following_card()
                last_play_card.clear()
                for card in main_player.pre_play_list:
                    last_play_card.append(card)
                return
            elif compare_card_list_size(last_play_numvalue_card, pre_play_numvalue_list,kind=kind):#上家的炸比
                display_word("Your Cards Lower Than Rival")
                return
        if kind==last_kind and \
                not compare_card_list_size(last_play_numvalue_card,pre_play_numvalue_list,kind=kind):
            #记得这里传的是numvalue比较的是对应的数值大小
            '''此时允许出牌，接下来写出牌的部分'''
            play_card_list(main_player)
            main_player_following_card()
            return
        elif kind!=last_kind:
            display_word("These Cards Not Allowed")
            return
        elif compare_card_list_size(last_play_numvalue_card,pre_play_numvalue_list,kind=kind):
            display_word("Your Cards Lower Than Rival")
            return
def click_suggest_button():
    if main_player.initiative==True:
        '''如果是主玩家起牌阶段'''
        '''规定建议主玩家起牌优先级：在不拆开炸弹的前提之下出尽量小的，
            顺子（拆完以后还有三连对）>三连对 > 三带二 > 三同张 > 三同连张 > 单张/对子按照0.5概率对分 > 最后炸弹
            当然了这个只是规则一，其实debug多了还发现，点数对其也有影响，也可以按照从小到大的顺序与优先级并结合概率来做'''
        hand_card_list_copy = Hand(main_player.hand_card_list.cards)
        hand_card_num_value_list_copy = [i.rank for i in hand_card_list_copy.cards]
        # 这里是对main_player手牌的一些操作
        hand_card_list_copy.refresh_available_card_combination()
        main_player.hand_card_list.refresh_available_card_combination()
        play_num_value = judge_shunzi_0(hand_card_list_copy=main_player.hand_card_list.card_combination)
        print("此时主玩家可以出的牌列表为：", play_num_value)
        play_cards = search_corresponding_card_list(main_player.hand_card_list.cards, play_num_value[0])
        print("主玩家此时建议打出的牌对象为：", play_cards)
        main_player.pre_play_list = play_cards
        for i in range(len(main_player.hand_card_list.cards)):
            if main_player.hand_card_list.cards[i] in play_cards:
                main_player.if_pre_play[i]=True
    elif main_player.following == True:
        '''如果是主玩家跟牌阶段'''
        last_kind=judge_card_kind(last_play_numvalue_card)
        '''规定建议主玩家跟牌规则优先级：尽量不出炸弹，设定一个出炸弹的概率函数，牌越少的时候出炸弹的概率越大
                跟的一定是相同牌型的牌/炸弹'''
        '''跟牌规则：设置一个有关于对方还有几张牌和出的牌的点数的概率函数  
           如果对方的牌数越少跟的概率就越高（当然权重比较小），如果对方牌的点数越小跟的概率也越高'''
        allow_list = []
        main_player.hand_card_list.refresh_available_card_combination()
        if last_kind == 1:
            allow_list = main_player.hand_card_list.card_combination["单张"]
        elif last_kind == 2:
            allow_list = main_player.hand_card_list.card_combination["对子"]
        elif last_kind == 3:
            allow_list = main_player.hand_card_list.card_combination["三同张"]
        elif last_kind == 4:
            allow_list = main_player.hand_card_list.card_combination["顺子"]
        elif last_kind == 5:
            allow_list = main_player.hand_card_list.card_combination["三连对"]
        elif last_kind == 6:
            allow_list = main_player.hand_card_list.card_combination["三带二"]
        elif last_kind == 7:
            allow_list = main_player.hand_card_list.card_combination["三同连张"]
        elif last_kind == 8:
            allow_list = main_player.hand_card_list.card_combination["炸弹"]
        # 判断是否可以出牌
        allow_play = False
        same_larger = False
        # main_player.pre_play_list=[]里面存的是对象！！！
        pre_play_numvalue_list = None
        print("主玩家允许出的牌列表为：", allow_list)
        print("AI出的牌为：", last_play_numvalue_card)
        for possible_list in allow_list:
            if not compare_card_list_size(last_play_numvalue_card, possible_list, kind=last_kind):
                allow_play = True
                same_larger = True
                pre_play_numvalue_list = possible_list
                break
        if not same_larger and last_kind != 8 and \
                main_player.hand_card_list.card_combination["炸弹"] != []:
            # 如果没有更大的牌了的话只有炸弹那就出炸弹
            bomb_num = len(main_player.hand_card_list.card_combination["炸弹"])
            allow_play = True
            pre_play_numvalue_list = main_player.hand_card_list.card_combination["炸弹"][0]
        if allow_play and same_larger:
            '''如果有同类型的可以更大的牌压住的话'''
            main_player.pre_play_list = search_corresponding_card_list(main_player.hand_card_list.cards, pre_play_numvalue_list)
        elif allow_play and not same_larger:
            '''如果没有同类型更大的牌但是有炸弹的话'''
            main_player.pre_play_list = search_corresponding_card_list(main_player.hand_card_list.cards, pre_play_numvalue_list)
        else:
            main_player.pre_play_list=[]
        for i in range(len(main_player.hand_card_list.cards)):
            if main_player.hand_card_list.cards[i] in main_player.pre_play_list:
                main_player.if_pre_play[i] = True
    print("摁下了建议键")




def AI_play_card_initiative_rules():
    '''使用神经网络预测其接下来出什么类型的牌'''
    max_num=0
    max_com=[]
    AI_state=process_state(AI.hand_card_num_value_list)
    main_state=process_state(main_player.hand_card_num_value_list)
    global count
    for kind in AI.hand_card_list.card_combination.values():
        for card in kind:
            if kind==[]:
                continue
            card1=process_card(card)
            data=card1+AI_state+main_state+[count]
            data=torch.tensor(data,dtype=torch.float32)
            with torch.no_grad():  # 确保不会计算梯度
                output = net(data)
            res = output[1].item()  # 转换为Python标准数据类型
            if res>=max_num:
                max_num=res
                max_com=card
    play_cards = search_corresponding_card_list(AI.hand_card_list.cards, max_com)
    print("此时AI出的牌为：", max_com,play_cards)
    AI.pre_play_list = play_cards
    play_card_list(AI)
    last_play_card.clear()
    for card in AI.pre_play_list:
        last_play_card.append(card)
    last_play_numvalue_card.clear()
    for card in AI.pre_play_list:
        last_play_numvalue_card.append(card.rank)
    pygame.time.delay(500)
    AI.hand_card_list.refresh_available_card_combination()
    draw_basic_background(screen=screen, main_player=main_player, AI=AI)
    # 接下来对自己和下一个人的牌权进行更新
    AI.initiative = False
    AI.following = False
    main_player.initiative = False
    main_player.following = True
    count+=1




def judge_shunzi_0(hand_card_list_copy):
    print("AI有的顺子为：",hand_card_list_copy["顺子"])
    if hand_card_list_copy["顺子"] != []:  # 如果有顺子
        #如果顺子里面有元素在炸弹里面则拒绝顺子准备出三连对
            if list1_element_in_list2(hand_card_list_copy["顺子"],hand_card_list_copy["炸弹"]):
                return judge_sanliandui_0(hand_card_list_copy)
            else:
                return hand_card_list_copy["顺子"]
    else:
        return judge_sanliandui_0(hand_card_list_copy)
def judge_sanliandui_0(hand_card_list_copy):
    ''''''
    print("AI有的三连对为：", hand_card_list_copy["三连对"])
    if hand_card_list_copy["三连对"] != []:
        if list1_element_in_list2(hand_card_list_copy["三连对"], hand_card_list_copy["炸弹"]):
            return judge_sandaier(hand_card_list_copy)
        else:
            return hand_card_list_copy["三连对"]
    else:
        return judge_sandaier(hand_card_list_copy)
def judge_sandaier(hand_card_list_copy):
    print("AI有的三带二为：",hand_card_list_copy["三带二"])
    if hand_card_list_copy["三带二"] != []:
        if list1_element_in_list2(hand_card_list_copy["三带二"], hand_card_list_copy["炸弹"]):
            return judge_santongzhang_0(hand_card_list_copy)
        else:
            return hand_card_list_copy["三带二"]
    else:
        return judge_santongzhang_0(hand_card_list_copy)
def judge_santongzhang_0(hand_card_list_copy):
    print("AI有的三同张为：", hand_card_list_copy["三同张"])
    if hand_card_list_copy["三同张"] != []:
        if list1_element_in_list2(hand_card_list_copy["三同张"], hand_card_list_copy["炸弹"]):
            return judge_santonglianzhang_0(hand_card_list_copy)
        else:
            return hand_card_list_copy["三同张"]
    else:
        return judge_santonglianzhang_0(hand_card_list_copy)
def judge_santonglianzhang_0(hand_card_list_copy):
    print("AI有的三同连张为：", hand_card_list_copy["三同连张"])
    if hand_card_list_copy["三同连张"] != []:
        if list1_element_in_list2(hand_card_list_copy["三同连张"], hand_card_list_copy["炸弹"]):
            return judge_single_or_double_0(hand_card_list_copy)
        else:
            return hand_card_list_copy["三同连张"]
    else:
        return judge_single_or_double_0(hand_card_list_copy)
def judge_single_or_double_0(hand_card_list_copy):
    print("AI有的对子有：", hand_card_list_copy["对子"])
    print("AI有的单张有：", hand_card_list_copy["单张"])
    #danzhang=[[single] for single in hand_card_list_copy["单张"]]
    if hand_card_list_copy["单张"] != [] and hand_card_list_copy["对子"] != [] and \
            not list1_element_in_list2(hand_card_list_copy["单张"], hand_card_list_copy["炸弹"]) and \
            not list1_element_in_list2(hand_card_list_copy["对子"], hand_card_list_copy["炸弹"]):
        rate=random.random()
        if rate<0.5:
            return hand_card_list_copy["单张"]
        else:
            return hand_card_list_copy["对子"]
    elif hand_card_list_copy["单张"] == [] or \
            list1_element_in_list2(hand_card_list_copy["单张"], hand_card_list_copy["炸弹"]):
        return hand_card_list_copy["对子"]
    elif hand_card_list_copy["对子"] == [] or \
            list1_element_in_list2(hand_card_list_copy["对子"], hand_card_list_copy["炸弹"]):
        return hand_card_list_copy["单张"]
    else:
        return hand_card_list_copy["炸弹"]


def AI_play_card_following_rules():
    '''在第二阶段AI跟牌的规则很简单，就是根据上一个回合种类将所有可能的出牌（同类型、炸弹、不出）
    投喂给神经网络，再根据生成的Q值选出最大的那个出'''
    hand_card_list_copy = Hand(AI.hand_card_list.cards)
    hand_card_num_value_list_copy = [i.rank for i in hand_card_list_copy.cards]
    #设置允许出的牌列表
    last_play_numvalue_card.clear()
    for card in last_play_card:
        last_play_numvalue_card.append(card.rank)
    last_kind = judge_card_kind(last_play_numvalue_card)
    allow_list = []
    if last_kind == 1:
        allow_list = AI.hand_card_list.card_combination["单张"]
    elif last_kind == 2:
        allow_list = AI.hand_card_list.card_combination["对子"]
    elif last_kind == 3:
        allow_list = AI.hand_card_list.card_combination["三同张"]
    elif last_kind == 4:
        allow_list = AI.hand_card_list.card_combination["顺子"]
    elif last_kind == 5:
        allow_list = AI.hand_card_list.card_combination["三连对"]
    elif last_kind == 6:
        allow_list = AI.hand_card_list.card_combination["三带二"]
    elif last_kind == 7:
        allow_list = AI.hand_card_list.card_combination["三同连张"]
    elif last_kind == 8:
        allow_list = AI.hand_card_list.card_combination["炸弹"]
    allow_list=set_allow_list(allow_list,last_kind)
    if last_kind !=8:
        allow_list+=AI.hand_card_list.card_combination["炸弹"]
    if allow_list==[]:
        allow_list.append([0,0,0,0,0,0])
    print("允许出的牌列表为：",allow_list)
    #接下来使用神经网络预测其接下来出什么类型的牌
    max_num = 0
    max_com = []
    AI_state = process_state(AI.hand_card_num_value_list)
    main_state = process_state(main_player.hand_card_num_value_list)
    global count
    for card in allow_list:
        if card == []:
            continue
        card1 = process_card(card)
        data = card1 + AI_state + main_state + [count]
        data = torch.tensor(data, dtype=torch.float32)
        with torch.no_grad():  # 确保不会计算梯度
            output = net(data)
        res = output[1].item()  # 转换为Python标准数据类型
        if res >= max_num:
            max_num = res
            max_com = card
    if max_com!=[0,0,0,0,0,0]:
        play_cards = search_corresponding_card_list(AI.hand_card_list.cards, max_com)
        print("此时AI出的牌为：", max_com, play_cards)
        AI.pre_play_list = play_cards
        play_card_list(AI)
        last_play_card.clear()
        for card in AI.pre_play_list:
            last_play_card.append(card)
        last_play_numvalue_card.clear()
        for card in AI.pre_play_list:
            last_play_numvalue_card.append(card.rank)
        pygame.time.delay(500)
        AI.hand_card_list.refresh_available_card_combination()
        draw_basic_background(screen=screen, main_player=main_player, AI=AI)
        AI_following_card()
    else:
        AI_not_following_card()



def AI_not_following_card():
    #如果AI选择不跟牌的话
    print("AI选择不跟牌")
    display_word("AI Choose Not Follow Cards")
    AI.initiative=False
    AI.following=False
    main_player.initiative=True
    main_player.following=False
    draw_basic_background(screen=screen, main_player=main_player, AI=AI)
    global count
    count += 1  # 回合数+1
def AI_following_card():
    # 如果AI选择跟牌的话
    AI.initiative = False
    AI.following = False
    main_player.initiative = False
    main_player.following = True
    draw_basic_background(screen=screen, main_player=main_player, AI=AI)
    global count
    count+=1#回合数+1
def main_player_following_card():
    # 如果main_player选择跟牌的话
    AI.initiative = False
    AI.following = True
    main_player.initiative = False
    main_player.following = False
    global count
    count += 1  # 回合数+1
def main_player_not_following_card():
    main_player.initiative = False
    main_player.following = False
    AI.initiative = True
    AI.following = False
    global count
    count += 1  # 回合数+1






def search_corresponding_card_list(cards,play_num_value):#返回对应的牌对象列表
    play_cards=[]
    #play_num_value_copy=play_num_value.copy()
    if isinstance(play_num_value, str):
        for i in range(len(cards)):
            if cards[i].rank == play_num_value:
                play_cards.append(cards[i])
                print("即将打出的牌为：", play_num_value)
                return play_cards
    for i in range(len(cards)):
        if cards[i].rank in play_num_value:
            play_cards.append(cards[i])
            play_num_value.remove(cards[i].rank)
    print("即将打出的牌为：",play_cards)
    return play_cards



def display_word(text_show):
    font = pygame.font.SysFont('Arial', int(size_of_screen_x / 15))  # 设置字体类型
    text = font.render(text_show, True, TransparentGreen)
    location = [size_of_screen_x*1/5, size_of_screen_y * 3 / 7]
    screen.blit(text, location)
    pygame.display.update()
    pygame.time.delay(1000)
def judge_card_kind(card_list):
    if len(card_list) == 1:
        return 1
    elif len(card_list) == 2 and \
            card_list[0] == card_list[1]:
        return 2
    elif len(card_list) == 3 and \
            card_list[0] == card_list[1] == card_list[2]:
        return 3
    elif len(card_list) == 5 and \
            card_list[0] == card_list[1] + 1 == card_list[2]+ 2 == \
            card_list[3] + 3 == card_list[4] + 4:
        return 4
    elif len(card_list) == 6 and \
            card_list[0]==card_list[1] == card_list[2]+ 1 == \
            card_list[3]+ 1 == card_list[4]+ 2 == card_list[5] + 2:
        return 5
    elif len(card_list) == 5 and \
            (card_list[0] == card_list[1] and card_list[2] == \
             card_list[3] == card_list[4] or card_list[0] == \
             card_list[1] == card_list[2] and \
             card_list[3] == card_list[4]):
        return 6
    elif len(card_list) == 6 and \
            card_list[0] == card_list[1] == card_list[2] == \
            card_list[3]- 1 == card_list[4] - 1 == card_list[5] - 1:
        return 7
    elif len(card_list) == 4 and \
            card_list[0] == card_list[1] == \
            card_list[2] == card_list[3]:
        return 8
    else:
        return 0
def compare_card_list_size(card_list1,card_list2,kind):######记住上家在前，下家在后并且传入的牌种类应当一样
    if isinstance(card_list2,str):
        if Card.dict_ranks[card_list1[0]] >= Card.dict_ranks[card_list2]:
            return True
        else:
            return False

    card_list1_copy=card_list1
    card_list2_copy=card_list2
    card_list1_copy.sort(reverse=True)
    card_list2_copy.sort(reverse=True)
    if kind == 6:
        if card_list1_copy[2]>=card_list2_copy[2]:
            return True###########################返回True表示1比2大，False表示1比2小
        else:
            return False
    if card_list1_copy[0]>=card_list2_copy[0]:
        return True
    else:
        return False
def play_card_list(player):#打出了牌
    first_card_loc=have_play_card_loc
    last_play_card.clear()
    for i in range(len(player.pre_play_list)):
        '''接下来使得card在中间即可'''
        url_card = player.pre_play_list[i].pict_path
        size = player.pre_play_list[i].size
        card_img = pygame.image.load(url_card).convert()
        card_img = pygame.transform.scale(card_img, size)
        card_loc = [first_card_loc[0]+i*delta_card,first_card_loc[1]]
        screen.blit(card_img, card_loc)
        last_play_card.append(player.pre_play_list[i])
        player.hand_card_list.cards.remove(player.pre_play_list[i])#从原来的地方删去这张牌
        player.have_card_num-=1
    for i in range(27):#将所有的牌重置
        player.if_pre_play[i] = False
    last_play_numvalue_card.clear()
    for card in last_play_card:
        last_play_numvalue_card.append(card.rank)
    draw_basic_background(screen=screen, main_player=main_player, AI=AI)


def display_have_played_card(have_play_card_list):
    '''显示已经被打出的牌'''
    first_card_loc=have_play_card_loc
    for i in range(len(have_play_card_list)):
        '''接下来使得card在中间即可'''
        url_card = have_play_card_list[i].pict_path
        size = have_play_card_list[i].size
        card_img = pygame.image.load(url_card).convert()
        card_img = pygame.transform.scale(card_img, size)
        card_loc = [first_card_loc[0]+i*delta_card,first_card_loc[1]]
        screen.blit(card_img, card_loc)
def list1_element_in_list2(list1,list2):#判断列表1中元素是否在二重列表2中
    for i in list1:
        for j in list2:
            if i in j:
                return True
    return False

def compare_two_size(list1,list2,kind):#上家在前，下家在后，大True小False
    '''"单"、"双"、"三同张"、"顺子"、"三连对"、"三带二"、"三同连张"、"炸弹"'''
    if kind==1 or kind==2 or kind==3 or kind==4 or kind==5 or kind==7:
        return list1[0]>list2[0]
    elif kind==6:
        if list1[0]>list2[0]:
            return True
        elif list1[0]==list2:
            return list1[4]>list2[4]
        else:
            return False
    elif kind==8:
        if len(list1)>len(list2):
            return True
        elif len(list1)==len(list2):
            if list1[0]>list2[0]:
                return True
            else:
                return False
        else:
            return False
def set_allow_list(input_list,last_kind):
    l=[]
    for i in input_list:
        if compare_two_size(i,last_play_numvalue_card,last_kind):
            l.append(i)
    return l


# 创建一个神经网络架构实例
net=NetWork()
# 加载保存的参数（使用状态字典）
net.load_state_dict(torch.load('net.pth'))
# 在eval评估模式下使用模型
net.eval()


def process_card(cards):
    '''对传入进来的牌进行处理'''
    # print("传入的cards为：",cards)
    if len(cards)>6:
        return cards[:6]
    return cards+[0]*(6-len(cards))
def process_state(state):
    '''对传入进来的状态进行处理'''
    return state+[0]*(27-len(state))



# 设置基本黑白颜色参数
Black=(0,0,0)
White=(255,255,255)
Red=(255,0,0)
Purple=(127,0,255)
TransparentGreen=(204,255,204)
PaleBlue=(153,153,255)
DarkRed=(51,0,102)
SkyBlue=(0,128,255)
# 设置基本窗口大小参数（这里默认窗口就用方形吧）
size_of_screen_x=800
size_of_screen_y=600
delta_card=size_of_screen_x/45#牌与牌之间空隙大小
# 初始化Pygame
pygame.init()
# 创建时钟对象
clock = pygame.time.Clock()
# 设置窗口大小
screen = pygame.display.set_mode((size_of_screen_x,size_of_screen_y))
# 设置窗口标题
pygame.display.set_caption("掼蛋游戏")
#初始化按钮类
play_button=Button(url_img="图片集\出牌.png")
giveup_button=Button(url_img="图片集\不出.png")
suggestion_button=Button(url_img="图片集\提示.png")
reset_button=Button(url_img="图片集\重置.jpg")
#初始化玩家类
url_steve="图片集\史蒂夫.jpg"
ulr_kulouma="图片集\骷髅马.jpg"
Steve_size=(size_of_screen_x/6,size_of_screen_y/4)
steve_loc=(0,size_of_screen_y-Steve_size[1])
kulouma_size = (size_of_screen_x / 6, size_of_screen_y / 4)
kulouma_loc=(0, 0)
main_player=Player(url_steve,steve_loc)
AI=Player(ulr_kulouma,kulouma_loc)
main_player.set_size(Steve_size)
AI.set_size(kulouma_size)
#初始化所有的牌
all_card_list=AllCards()
print("所有的牌为：",all_card_list.cards_list)
#初始化玩家和AI的牌  各获得27张牌
playerlist=all_card_list.cards_list[0:27]
AIlist=all_card_list.cards_list[27:54]
main_player.set_hand_card_list(Hand(playerlist))
AI.set_hand_card_list(Hand(AIlist))
main_player.hand_card_list.print_all_card_name()
AI.hand_card_list.print_all_card_name()
print("玩家拥有的牌为：",main_player.hand_card_num_value_list)
print("AI拥有的牌为：",AI.hand_card_num_value_list)
main_player_card_loc=(steve_loc[0]+Steve_size[0]+delta_card/2,steve_loc[1])
main_player.determine_first_card_location(main_player_card_loc)
AI_card_loc=(kulouma_loc[0]+kulouma_size[0]+delta_card/2,kulouma_loc[1]+30)
AI.determine_first_card_location(AI_card_loc)
#初始化出牌区的位置
have_play_card_loc=[size_of_screen_x*1/5, size_of_screen_y * 3 / 7]
# 游戏开始先发牌
count=1
# 输出发牌阶段
'''以下写GUI发牌阶段操作'''
# 接下来开始理牌
'''以下写GUI理牌操作'''
main_player.hand_card_list.sort_hand_card()
AI.hand_card_list.sort_hand_card()
#接下来确定牌权
priority_play_card=determine_priority(AI=AI)#priority_play_card表示牌权 True表示在我方 False表示在对方 有大王一方拥有牌权
AI.initiative =AI.following= main_player.initiative = main_player.following =False #初始化所有均为False
if priority_play_card:#这里的initiative与following分别代表接下来是否为起牌跟牌阶段
    print("主玩家拥有牌权")
    main_player.initiative=True
else:
    print("AI拥有牌权")
    AI.initiative = True
# 游戏循环
done = False
winner=None
mouse_loc=(0,0)
last_play_card=[]#上一名玩家出的牌（存储的是对象）
last_play_numvalue_card=[]#上一名玩家出的牌（存储的是点数比如"K"）
draw_basic_background(screen=screen,main_player=main_player,AI=AI)
pygame.display.update()
pygame.time.delay(500)
while not done and winner==None:
    # 判定赢家
    if main_player.hand_card_list.cards == []:
        winner = main_player
    elif AI.hand_card_list.cards == []:
        winner = AI
    #判断是否摁下了退出键
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ''''''
    # 主玩家起牌阶段
    if main_player.initiative:
        '''主玩家起牌阶段'''
        main_player_initiative()
    # AI起牌阶段
    if AI.initiative:
        '''AI起牌阶段并且此时AI不是跟牌'''
        AI_initiative()
    # 主玩家跟牌阶段
    if main_player.following:
        '''此时为主玩家跟牌阶段'''
        main_player_following()
    # AI跟牌阶段
    if AI.following:
        '''此时为AI跟牌阶段'''
        AI_following()

    # 更新窗口
    pygame.display.update()
    # 判断输赢
    # 控制游戏帧率
    clock.tick(60)
if winner==main_player:
    display_word("Congratulations You Win")
elif winner==AI:
    display_word("Sorry You Lose")
#退出Pygame
pygame.quit()















