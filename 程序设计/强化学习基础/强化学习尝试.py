#强化学习相当于一个自学程序
''''''
'''
Q-Learning：
Q(s,a)<-Q(s,a)+alpha[ r + gamma * maxQ(s',a')-Q(s,a)]
ACTIONS=["Left","Right"] #允许的行为
N_STATES=6  #允许的状态个数
EPSILON=0.9  #greedy police选择最优策略概率
ALPHA=0.1    #学习率learning rate
LAMBDA=0.9  #discuont factor对未来奖励的衰减度
MAX_EPISODES=13  #maximum episodes最大只玩13回合
FRESH_TIME=0.3  #fresh time for one more
'''

