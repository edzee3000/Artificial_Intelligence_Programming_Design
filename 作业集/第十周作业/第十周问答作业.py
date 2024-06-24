

#举例说明python实现多态
class Creature:
    def __init__(self):
        self.lifelong=100
        self.name="鲸鱼"
        self.food="鱼虾"
    def eat_food(self):
        print(f"{self.name}吃{self.food}")
class Human(Creature):
    def __init__(self,name:str="人类",food:str="什么都吃"):
        super().__init__()
        self.name="人类"
        self.food="什么都吃"
    def eat_food(self):
        print(self.food)
        print("此处发生了重写overriding实现了多态")

#print(Human.__doc__)
#print(Human.__annotations__)

def set_person():
    try:
        person1=Human()
        person1.name="朱士杭"
        return
    except Exception:
        pass
    else:
        pass
    finally:
        print("当在try语句中return之后finally语句仍旧会执行")
        pass
set_person()

