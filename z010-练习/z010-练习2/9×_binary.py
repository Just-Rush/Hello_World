"""十进制转换成二进制"""
"""!!!"""
num = int(input("输入要转化的数字："))
# i = 0
# while True:
#     if num-2**i != 0 and num-2**i != 1:  # 一开始用的or，半天没找到问题，与或非 要熟练
#         i = i+1
#     else:
#         break
#     print(i)
# remainder = num % 2**i
# num2 = 1*10**i + remainder
# print(num2)
"""错错错"""
"""还是看了要用列表才会做的"""
"""很多问题要用列表解决啊"""
list0 = []
while True:
    if num/2 >= 2:
        list0.append(1)
        num = num/2
    elif num/2 == 1:
        list0.append(1)
        list0.append(0)
        break
    elif num == 0:
        list0.append(0)
        break
print(list0)
a = ",".join(str(element) for element in list0)
print(a)



