'''
[],定义列表
.append(),.insert() 添加、插入列表
修改，直接 =
del 变量名[索引],.pop(索引，默认为末位),.remove(值)  删除列表

'''


#练习3.4 嘉宾名单
dinner_list = ['狗哥','ab','ysh',]
print(dinner_list)
print(dinner_list[0])
message1 = f"欢迎{dinner_list}来做客"
print(message1)
message2 = f'欢迎{dinner_list[1]}来玩'
message3 = f"欢迎{dinner_list[2].title()}来打游戏"
print(message2,message3)

#练习3.5 修改嘉宾名单
print(f'很遗憾，{dinner_list[2]}有事来不了')
dinner_list[2] = 'hhx'
print(f'我重新邀请了{dinner_list[2]}来')

#练习3.6 我现在准备多情几个人吃饭
dinner_list.insert(0,'cn')
dinner_list.append("lyx")
dinner_list.insert(2,'rr')
print(f'欢迎{dinner_list}来做客')
#    如何用循环写出一个每个名字分别邀请的呢？
for name in dinner_list :#这个地方不太懂，等于是将list里的变量重新命名为name了吗，
    message_content = '欢迎'+ name+"来我家吃饭"
    print(message_content)
#    一定注意这个print一定要在for循环内，否则就只能答应一个，而且是最后一个（不知道为啥是最后一个）。因为循环的终值是最后一个

#练习3.7 缩短名单 爷不请客了
popped_1 = dinner_list.pop()
print(popped_1 + '说不来')
popped_2 = dinner_list.pop()
print(f'{popped_2}说不来')
#    这个地方也应该用循环才好
print('小爷生气了，现在只请两个人吃饭')
del dinner_list[0]
dinner_list.remove('ab')
print('就决定是你们两个了')
for name1 in dinner_list :
    print(name1)
#    这个地方如何让他们和上面那个句子都是一排的,print语句里怎么不能直接写东西

del dinner_list[0]
del dinner_list[1]
print(dinner_list)
#    这个地方很奇怪，当dle dinner_list[0,1]的时候，会报错，说不能是复数，但是当鼠标点到这行代码的时候就不会报错并且正常运行
'''为什么有时候是斜体有时候不是啊，烦
管理列表
'''


