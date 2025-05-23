# #练习4.3----------每个都要3步，能不能优化啊
# numbers1 = range(1,21)
# for number1 in numbers1:
#     print(number1)
#
# #练习4.5
# numbers2 = list(range(1,1000001))
# print(min(numbers2))
# print(max(numbers2))
# print(sum(numbers2))
#
# #练习4.6
# numbers3 = list(range(1,21,2))
# for number3 in numbers3:
#     print(number3)

# #练习4.7
# numbers = list(range(3,31,3))
# for number in numbers:
#     print(number)

#练习4.8
# numbers = list(range(1,11))
# for number in numbers:
#     value = number**3
#     print(value)
# numbers1 = []
# for number1 in range(1,11):
#     value1 = number1**3
#     print(value1)
#     numbers1.append(value1)#注意这里要放进循环，才可以将每一个都添加进列表。
# print(numbers1)

#练习4.9
numbers = [value**3 for value in range(1,11)]
print(numbers)
for number in numbers:
    print(number)


