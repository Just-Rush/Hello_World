# # 练习 4.10
# numbers1 = []
# for number1 in range(1,11):
#     value1 = number1**3
#     print(value1)
#     numbers1.append(value1)
# print('the first three items in the list are')
# print(numbers1[0:3])
# print('three items from the middle of the list are')
# print(numbers1[3:6])
# print('the last are')
# print(numbers1[-3:])

'''有没有什么办法可以使打印出来的在一行呢，而且不含列表的中括号------不含中括号就要赋值，使变量不为列表，在一起，就应该用f语句'''
# print(f'the last are {numbers1[-3:]}')#这里仍是列表，所以不行
#
# # print('the last are' + number),这种语法不合法，但是又老爱这么搞，不知道哪里学的。要用f语句
# for value2 in numbers1[-3:]:
#     print(f'the last are {value2}')
# #多写几个单独赋值肯定行，但是太麻烦了。暂停，



# 练习 4.11
my_stuff = ['a','b','c']
friends_stuff = my_stuff[:]
my_stuff.append('d')
friends_stuff.append('e')
print('my stuff have ')
for stuff in my_stuff:
    print(stuff)

print('my friends stuff have')
for stuff1 in friends_stuff:
    print(stuff1)

'''
使用切片时是创建的副本，也即是两个不同的列表了，互相独立，赋值的时候就是指向同一个列表。
！
'''





