#6.1
gouge = {'first_name': 'zhang',
          'last_name': 'mingsheng',
          'age': '24',
          'city': 'beiing',
          }
for value1 in gouge:
    print(value1)
#   错误，for循环在字典中只循环键
for value in gouge.values():
    print(value)
#   方法1
print(gouge.values())
#   方法2，6.2后想到，哎
for k in gouge:
    print(gouge[k])

'''
不懂的可以多上网查，有时候不是脑子想不到只是没有这个知识储备
要用简单的代码全部打印出来只需要用.value()函数+for循环就可以了，没有.value()时就只打印键
'''

#6.2
figure = {'哈哥':1,'狗哥':2,'轩总':3,'ab':4,'晏骚':5}
for k in figure:
    print(k,'喜欢',figure[k])
    print(f'{k}喜欢{figure[k]}')
'''
又是查的，哎感觉我好呆啊------也可能是书上还没到对应部分，但是之前也看了些视频的，抽烟，视频短看得也不够认真，练习做的也不够，时间也过了比较久吧，
哎，多练多学。书上的意思也有可能是说一个一个打？因为后面才讲的遍历字典------确实是这样的，大概只是因为我还没看到。后面的练习才明确说了用for循环
所以不是我呆，而是我爱思考
for k in figure:
    这个就是对字典中的键遍历---bingo，等同于.keys()方法
print(k,'喜欢',figure[k])
    k就是变量键，figure[k]就是字典中键对应的值
那6.1也能改
'''

#6.5
rivers= {'尼罗河':'埃及','长江':'中国','莱茵河':'德国','恒河':'印度'}
for river,country in rivers.items():
    print(f'the {river} runs through {country}')
 



