"""
#Book类模拟图书借阅过程
class Book:
    is_borrowed=False
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.borrower_history = []
    def borrow_book(self,borrow_name):
        '''借书的成员函数/方法'''
        if self.is_borrowed==True:
            len_his=len(self.borrower_history)
            print(f"{self.title}这本书已经被{self.borrower_history[len_his-1]}借走啦")
        else:
            self.is_borrowed=True
            self.borrower_history.append(borrow_name)
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed=False
        else:
            print(f"{self.title}这本书还未被借出去")
    def get_borrow_history(self):
        if self.borrower_history!=[]:
            print(f"所有借阅过{self.title}这本书的有：",self.borrower_history)
        else:
            print(f"{self.title}这本书至今仍未被借出去过")
    def print_is_borrowed(self):
        if self.is_borrowed:
            print(f"{self.title}这本书已经被借出去啦")
        else:
            print(f"{self.title}这本书还未被借出去")
#创建三本书的实例
book_list=[]
book_list.append(Book("《必有人重写爱情》","北岛"))
book_list.append(Book("《人工智能：一种现代方法（第四版）》","斯图尔特·罗素"))
book_list.append(Book("《黄金时代》","王小波"))
#一本书被同一个人多次借阅和归还
print("****接下来测试一本书被同一个人多次借阅和归还的场景****")
book_list[2].borrow_book("王二")
book_list[2].print_is_borrowed()
book_list[2].return_book()
book_list[2].print_is_borrowed()
book_list[2].borrow_book("王二")
book_list[2].borrow_book("王二")
book_list[2].return_book()
book_list[2].get_borrow_history()
#尝试借已经被借出的书
print("****接下来测试尝试借已经被借出的书的场景****")
book_list[0].borrow_book("朱士杭")
book_list[0].borrow_book("Edison")
#打印借阅历史记录
print("****接下来测试打印借阅历史记录的场景****")
for i in book_list:
    i.get_borrow_history()
"""



"""
# make_filter高阶函数
def make_filter(condition):
    def filter_list(lst):
        # 实现过滤逻辑
        # 核心思路：如果满足条件（True），则保留，不满足则删除
        return [i for i in lst if condition(i)]  # 删除这一行，并添加适当的代码
    return filter_list
def is_even(number):
    return number % 2 == 0
# 使用 make_filter 创建过滤器
even_filter = make_filter(is_even)
# 测试 even_filter
test_list = [1, 2, 3, 4, 5, 6]
filtered_list = even_filter(test_list)
print(filtered_list)  # 应该输出 [2, 4, 6]
"""



