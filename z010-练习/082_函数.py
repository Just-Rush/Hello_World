#8.9
def show_messages(messages):
    for message in messages:
        print(f'{message}')

a = ['你好','他好','我也好']
show_messages(a)

#8.10
b = []
def send_messages2(show_messages,sent_messages):
    while show_messages:#这个用法还蛮重要的，要记住，当列表为空集时布尔值就为False了,否则为True，列表就会一直运行
        sent_message = show_messages.pop(0)#给。pop加个索引使从第一个开始删减，否则最后出来的结果会是与列表相反的顺序
        sent_messages.append(sent_message)
        print(sent_message)
    print(sent_messages)
    print(show_messages)
send_messages2(a,b)

def send_messages(show_messages,sent_messages):
    for message in show_messages:
        sent_messages.append(message)
        show_messages.remove(message)
    print(show_messages)
    print(sent_messages)
A = ['1','2','3']
B = []
send_messages(A,B)
'''使用for循环怎么就不对头呢,为什么会剩一个中间的东西remove不掉呢
搞懂了，循环时是
按照第一个，第二个的顺序来检索列表内容
循环中的列表的第一个变量是1，1进入循环，s_m.append(1)，1被添加进sent_m列表，同理，1在show_m中被删除
此时循环列表中的第二个变量，由于列表出现了增减，此时show_m列表中元素为[2,3]，其中的第二个变量为3
所以此时3进入了循环，2被轮空，导致了这个结果发生。
即便是使用.pop(0)也不能避免，因为改变了列表，在for循环时检索的顺序就不同了。
上面用while循环的逻辑就不太一样。
这么看来在对列表有删减时，使用while循环也更优。
'''

#8.11------创建一个副本进行替代即可
def send_messages3(show_messages,sent_messages):
    show_m_copy = show_messages[:]
    while show_m_copy:
        sent_message = show_m_copy.pop(0)
        sent_messages.append(sent_message)
        print(sent_message)
    print(sent_messages)
    print(show_messages)
aa = [1,2,3]
bb = []
send_messages3(aa,bb)