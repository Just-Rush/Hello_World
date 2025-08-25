#5.2
a = ['a','b','c']
aa = 'c'
aaa = 'd'
if (aa not in a) and (aaa not in a):
    print('aa is not in a')
else:
    print('aa is in a')

#5.5
aline_color = 'red'
if aline_color == 'green':
    grade = 5
elif aline_color == 'yellow':
    grade = 10
elif aline_color == 'red':
    grade = 15
print(f'you get {grade} score')

#5.6
age = 66
if age < 2:
    stage = '还是一个婴儿'
elif age < 13:
    stage = '还是儿童'
elif age < 18:
    stage = '还是少年'
elif age < 65:
    stage = "已经中年了"
else:
    stage = '已经是老年人了'
print(f'这个人现在{stage}')
'''
可以把print放在每一个函数的下面替换stage，但是这样毫无疑问要简洁些
然后感觉这个是不是可以优化一下成什么循环，因为这样要写好多个elif
# '''

#5.7
favorite_fruits = ['apple','banana','watermelon']
if 'apple' in favorite_fruits:
    print('you really like apple')
if 'banana' and 'watermelon' in favorite_fruits:
    print('you also like banana and watermelon')


#5.8
list1 = ['aaa','b','c','d','e']
# list1 = []
if list1:#检查列表是否为空
    for name1 in list1:
        if name1 == 'aaa':
            print('hello,aaa,you are the powerful pokemon trainer')
        else:
            print(f'hello {name1},thank you for your efforts,but it\'s a pity that you failed')
else:
    print('啊啊啊')

#5.9
current_users = ['f','g','h','i','j','k']
new_users = ['J','k','l','m','n']
users1 = [name.lower() for name in current_users]
users2 = [name2.lower() for name2 in new_users]
for user in users2:
    if user in users1:
        print(f'your name {user} had been used,you need to input other name to continue')
    else:
        print(f'your name \'{user}\' is ...,thank you for your support')
'''
列表推导式里面也可以放函数，不仅仅是可以做计算，太牛了
这么写虽然可以避免大小写问题，但是感觉麻烦了点，怎么优化一下呢？书上说的创建一个副本包含全小写版本是什么意思呢？
错误的，并没有能避免大小写问题，因为在输出时将J输出成j了，下面这个是可以的。这么搞是叫副本吗
'''
current_users = ['f','g','h','i','j','k']
new_users = ['J','k','l','m','n']
users1 = [name.lower() for name in current_users]
for user in new_users:
    if user.lower() in users1:
        print(f'your name {user} had been used,you need to input other name to continue')
    else:
        print(f'your name \'{user}\' is ...,thank you for your support')

'''
结合input编写一个游戏里的取名字的系统
应该要结合while循环
'''
# name = input('请输入你的昵称：')
# name_lists1 = ['aaa']
#
# if name not in name_lists1:
#     name_lists1.append(f'{name}')
#     print(f'您的新昵称为{name}')
#
# elif name in name_lists1:
#     name = input('该昵称已存在，请修改你的昵称：')
#     while name not in name_lists1:
#         print(f'您的新昵称为{name}')
#         name = []

