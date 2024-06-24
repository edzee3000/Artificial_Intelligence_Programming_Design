



def improve(update,accurate,guess):
    '''迭代函数'''
    while not accurate(guess):
        guess = update(guess)
    return guess
#接下来尝试用算出根号x
def square_x(x):
    def square_update(guess):
        '''这里写的是对范围进行收缩，guess默认初始化为[0,x]'''
        if  average(guess)**2>=x:
            return guess[0], average(guess)
        else:
            return average(guess),guess[1]
    def accurate_square(guess):
        return abs(average(guess)**2 - x) < 1e-10
    def average(guess):
        return (guess[0]+guess[1])/2
    return average(improve(square_update,accurate_square,(0,x)))

print(square_x(2))
