

#请分别使用递归和非递归的方式，实现反转字符串的功能，请比较递归和非递归方式的区别
#非递归方式实现反转字符串功能
def Not_recursion_reverse_str(str_input):
    '''循环实现反转字符串'''
    str_list=list(str_input)
    str_list.reverse()
    new_str="".join(str_list)
    return new_str
def recursion_reverse_str(str_input):
    '''递归实现反转字符串'''
    if str_input=="":
        return ""
    return str_input[len(str_input)-1] + recursion_reverse_str(str_input[0:len(str_input)-1])





import doctest
#设计一个Python程序来管理图书馆中的图书
def append_new_book(books_shelves,bookname,author,rented=False):
    '''
    >>> append_new_book(books_shelves,"ILoveNanjing","Lizhi")
    {'ILoveNanjing': ['Lizhi', False]}

    :return:dict
    '''
    books_shelves[bookname]=[author,rented]
    return books_shelves
def renew_book_state(books_shelves,bookname,rented):
    '''
    >>> renew_book_state(books_shelves,"ILoveNanjing",True)
    更新 ILoveNanjing 的借阅状态为：已借阅
    {'ILoveNanjing': ['Lizhi', True]}
    >>> renew_book_state(books_shelves,"ILoveNanjing",False)
    更新 ILoveNanjing 的借阅状态为：已归还
    {'ILoveNanjing': ['Lizhi', False]}

    :param dict:
    :param str:
    :param bool:
    :return:None
    '''
    whether_rented = rented
    if whether_rented:
        whether_rented = "已借阅"
    else:
        whether_rented = "已归还"
    books_shelves[bookname][1]=rented
    print(f"更新 {bookname} 的借阅状态为：{whether_rented}")
    return books_shelves
def inquire_book(books_shelves,bookname):
    '''
    >>> inquire_book(books_shelves,"ILoveNanjing")
    作者名字为：Lizhi 借阅状态为：已归还

    :param dict:
    :param str:
    :return: None
    '''
    if bookname not in books_shelves.keys():
        print(f"{bookname} 无法查询得到")
        return
    author=books_shelves[bookname][0]
    whether_rented=books_shelves[bookname][1]
    if whether_rented:
        whether_rented="已借阅"
    else:
        whether_rented="已归还"
    print(f"作者名字为：{author} 借阅状态为：{whether_rented}")
def display_all_books(books_shelves):
    '''
    >>> display_all_books(books_shelves)
    图书名字为：ILoveNanjing 作者名字为：Lizhi 借阅状态为：已归还

    :param dict:
    :return:None
    '''
    for (k,v) in books_shelves.items():
        whether_rented = v[1]
        if whether_rented:
            whether_rented = "已借阅"
        else:
            whether_rented = "已归还"
        print(f"图书名字为：{k} 作者名字为：{v[0]} 借阅状态为：{whether_rented}")
    return

if __name__=="__main__":
    books_shelves={}
    # append_new_book(books_shelves,"我爱南京","李志")
    # print(books_shelves)
    # renew_book_state(books_shelves,"我爱南京",True)
    # inquire_book(books_shelves,"我爱南京")
    # display_all_books(books_shelves)
    doctest.testmod(verbose=True)











