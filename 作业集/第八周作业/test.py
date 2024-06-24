


''''''
'''
class Song:
    def __init__(self,name,singer):
        self.__name=name
        self._singer=singer
nj=Song("music","singer")
print(nj._singer)
#print(nj.__name)
'''


'''
class Account:
    def printInfo(self):
        print("Base.Name.Balance")
class CheckingAccount(Account):
    def printInfo(self):
        Account.printInfo(self)
        print("CheckingAcount info.")
class SavingsAccount(Account):
    def printInfo(self):
        Account.printInfo(self)
        print("SavingAcount info.")
class NewAccount(CheckingAccount, SavingsAccount):
    def printInfo(self):
        Account.printInfo(self) #?
        CheckingAccount.printInfo(self) #?
        SavingsAccount.printInfo(self) #?
        print("NewAcount info.")
a=NewAccount
NewAccount.printInfo(a)
'''




def greeting(name: str) -> str:
    return 'Hello ' + name
print(greeting(2))








