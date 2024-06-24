# def fib(n):
#     if n==1 or n==2:
#         return 1
#     return fib(n-1)+fib(n-2)
# print("在test.py文件中Fibonacci数列输入10结果为：",fib(10))




# import numpy as np
# myarray = np.arange(100).reshape(10, 10)
# # print(myarray)
# # print(myarray[: ,1])
# # print(myarray[-3:,-3:])
# # print(myarray[:,-3:])
# # print(myarray[-3:])
# # newarray =myarray[::5,-3:]
# arr1=np.arange(0,10).reshape((2,5))
# # print(arr1)
# arr2=np.arange(100,95,-1).reshape((1,5))
# arr3=np.vstack((arr1,arr2))
# # print(arr3)
# arr3=np.append(arr1,arr2)
# # print(arr3.reshape(3,5))
#
#
# all_cards=np.append(np.arange(3,16,1).repeat(8),np.arange(16,18).repeat(2))
# np.random.shuffle(all_cards)
# all_cards=all_cards.reshape((2,54))
# # print(all_cards)
# # print(np.array(all_cards))
# # print(np.array([0]).repeat(5))
# arr=np.array([1,1,1,2,3,4])
# arr=np.delete(arr,np.where(arr==1)[0][0])
#
# # print(arr)
#
# import pandas as pd
# df1 = pd.DataFrame(np.random.randn(0, 5), columns=["玩家","我方牌序列","对方牌序列","胜负","Q值"])
# # print(df1)
# a=[0,"1",2,3,True]
# df1.loc[len(df1)]=a
# # print(df1)
#
# # bb = {'a': 5.0,
# #       'b': 1.189692017587326,
# #       'c': 22,
# #       'd': 1.152140099155294,
# #       'e': 3.276673404529217,
# #       'f': 1.709932580576279,
# #       'g': 0.9993713969313217}
# # df.loc[len(df)] = bb
#
#
#
# # 加载模型参数
# model = SimpleNet(input_size, hidden_size, output_size)  # 假设 SimpleNet 是你的模型类
# model.load_state_dict(torch.load('model.pth'))
#
# # 如果你保存了整个模型
# # model = torch.load('complete_model.pth')
#
# # 将模型设置为评估模式
# model.eval()
#
# # 确保在测试或推理时不计算梯度
# with torch.no_grad():
#     # 使用加载的模型进行预测
#     predictions = model(x_test)





import numpy as np
import pandas as pd

# arr=np.array([[0,1,2],
#               [3,4,5]])
# arr=arr.transpose()
# arr=arr.reshape(1,6)
# print(arr)



























