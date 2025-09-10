#7.5
''
# word = ''
# while word != 'q':
#     fees = int(input('请输入你的年龄，以便返回您的票价：'))
#     if fees < 3:
#         print('您的年龄小于3岁，将不收取票价')
#     elif 3 <= fees < 12 :
#         print('您的年龄小于12岁，收取票价为12')
#     elif 12< fees:
#         print('您已年满12周岁，收取票价为15')
#这个好像就不用单独设一个终止的了，因为不会一直循环下去，用户输入一个就返回一个，挺好。
'''我这个用一个变量保证循环能够开始的做法合理吗，可以更改吗？------要想循环一直运行可以直接使用 while True:
显然不合理，因为进入循环就出不来了，不能再运行 while循环 后面的语句了
改也好改，用int(fees)去做比较即可，再加一个输入q时结束运行
但是始终不够好
要用条件测试就把fees换成word就可以了，然后数据类型改一改，跟下面那个用标志的方法差不多'''
'''但是要想结束显然就要有一个什么条件的啊'''
active = True
while active:
    fees1 = input("请输入您的年龄，将返回您的票价\n输入q返回\n")
    if fees1 == 'q':#这个地方要把他放在第一行，否则若在elif中因为输入的q为float类型，变不了int，将无法与数字进行比较而报错
        active = False
    elif int(fees1) < 3:
        print('您的年龄小于3岁，将不收取票价')
    elif 3 <= int(fees1) < 12:
        print('您的年龄小于12岁，收取票价为12')
    elif 12 < int(fees1):
        print('您已年满12周岁，收取票价为15')
print('感谢您的使用')

#使用break
# fees_2 = ''
# while fees_2 != 'q':
#     fees_2 = input('请输入您的年龄')
#     if fees_2 == 'q':
#         break
#     elif int(fees_2) <= 3:
#         print('免票')
#     elif int(fees_2) <= 12:
#         print("票价为10元")
#     elif int(fees_2) > 12:
#         print('票价为15元')
# print('感谢您的使用欢迎下次光临')
'''或者是直接用 while True: 打头，同样的'''
while True:
    fees_2 = input('请输入您的年龄')
    if fees_2 == 'q':
        break
    elif int(fees_2) <= 3:
        print('免票')
    elif int(fees_2) <= 12:
        print("票价为10元")
    elif int(fees_2) > 12:
        print('票价为15元')
print('感谢您的使用欢迎下次光临')

