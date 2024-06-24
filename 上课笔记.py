

'''汉诺塔freestyle搜索问题 BFS与DFS'''



#2024.04.02 函数深入理解
'''
函数式执行环境：用环境来解决名字的绑定问题
使用frame帧/栈帧（相当于C++中的作用域scope）描述python代码的执行环境
每个frame中包含独立的绑定关系（变量、函数等）
C++里面有：全局作用域、局部作用域、文件作用域、类作用域、命名空间作用域……
python里面有：global全局帧、local局部帧

程序执行的第一个frame为global frame全局作用域
函数调用的时候为被调用的函数创建frame，记录形参与实参的绑定关系，记录函数执行过程中发生的新绑定
在使用变量名的时候依次在local frame局部作用域、global frame全局作用域中寻找绑定
函数每次调用创建的是独立的local frame互相之间不影响

pure-function：函数执行过程不影响函数外部的状态
non-pure-function：函数执行过程会产生副作用，对外部状态产生影响

不可变immutable参数类似于C++里面值传递，mutable参数传递类似于C++里面的址传递

python里面对于同一个变量绑定一定在同一个frame 比如print(x) x=5会报错
如何在函数中修改环境中的值（绑定关系）：global x 显示声明需要修改的绑定关系

算法正确性：任意一个合法的输入经过有限步执行之后算法应给出正确的结果
算法正确 vs 程序正确：输入输出结果与预期是否一致
保证程序正确性的方法：①形式化验证formal verification②程序分析（动态分析、静态分析）③软件测试

编写测试函数，保证函数正确性  assert语句 assert function(arg1,arg2)==(res1,res2),'错误提示'
testmod以交互模式去测试

'''













