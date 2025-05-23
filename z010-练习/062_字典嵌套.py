#6.7
disposition_1 = {'主板':'B760小雕','CPU':'14600K'}
disposition_2 = {'主板':'B760小雕','CPU':'14600KF'}
disposition_3 = {'主板':'Z790小雕','CPU':'14600K'}
disposition_4 = {'主板':'Z790小雕','CPU':'14600KF'}
disposition_5 = {'主板':'Z790小雕','CPU':'13600KF'}
motherboard_and_CPU_lists = [disposition_1,disposition_2,disposition_3,disposition_4,disposition_5]

for disposition_serial_number in motherboard_and_CPU_lists:
    #print(disposition_serial_number)#这里变量指代了字典，打印出来就是字典的内容而不是字典的名字了
    print(disposition_serial_number['主板'],disposition_serial_number['CPU'])#因为变量指代字典，所以加 [键] 就指代字典的值了

for serial_number,disposition in motherboard_and_CPU_lists:#在这里两个变量就分别指代了列表中字典前后的两个键
    print(serial_number,disposition)
    print(serial_number[0])#变成了键的第一个字。
#如果要同时打印出是第几个配置，同时配置的内容是什么，应该怎么做

'''
这样好像必须要自己用文字来描述，比如f'主板是{}，CPU是{}'这样
写在字典里的键，字典的名字只是为了自己好理解？------错误的，应该用.item()方法，学得太烂了
下面这样利用两个循环可以勉强做到，但是仍然打不出是第几个配置
'''
for a in motherboard_and_CPU_lists:
    for n,d in a.items():#.item()方法---返回字典的键值对,所以就是对应键与值了
        print(n,d)


