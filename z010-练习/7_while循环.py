"""while与for循环一般可以相互替代
但是在已知需要循环多少次时，for循环往往比while循环简单一些
未知需要循环多少次时，则while更好一些
!!!while要注意要写i=i+1之类的!!!，否则可能一直为真，for循环等于是自己有个这么处理的步骤"""
#上面那个字体是怎么回事
#设计一个计算用户输入任意数量数字，计算其平均值的计算器，最后输入q时给出平均值
print("这是一个计算平均值的计算器，请输入数字进行计算，输入完毕后输入q进行计算：")
i = input("您输入的第1个数字为：")
number = 0
total = 0
#实际上前面只是在定义变量，尤其是那个i
while i != "q":
    number = number+1
    total = total+int(i)
#这个地方少了一个对i重新赋值的命令，导致i没有进入循环
    i = input("您输入的第" + str(number+1) + "个数字为：")
if number == 0:
    result = 0
else:
    result = total/number   #这个result要放在else里面，否则就是单独的一个没有意义的命令了。因为是先有的这个计算，再加的分母为0的判断，所以一开始这一句话不在else里导致报错
print("结果为" +str(result))

'''如果要使为，
您输入的第一个数字为
您输入的第二个数字为
这样，又应该如何设计呢
已成功设计'''
# total = 0
# count = 0
# i = input("请输入数字（完成输入后输入q终止程序）：")
# while i != "q":
#     num = float(i)   这一步是把input输入的字符串转化成浮点数，但是上面那个没有转化也没有问题。
#                      应该是有什么优化，另外在对i赋值时就赋值成浮点数应该也是可以的吧
#     total += num
#     count += 1
#     i = input("请输入数字（完成输入后输入q终止程序）：")
# result = total/count
# print("您输入的数字平均值为：" + str(result))
