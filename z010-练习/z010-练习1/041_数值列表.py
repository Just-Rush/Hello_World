#使用list函数可直接将range()的结果转化成清单
numbers = list(range(1,10,2))
print(numbers)
'''使用range()函数可创建几乎任意的数值组合清单（列表）'''
squares = []#创建一个空列表
for value in range(1,10,2):
    square = value**2
    squares.append(square)#将计算得到的平方值追加到空列表内，因为在for循环里，所以每一个都会添加进去
print(squares)
'''暂时没想到其他的方法，提前创建一个空列表很重要------艹但是书上给了更简洁的，不用中间变量'''
squares2 = []
for value2 in range(1,11):
    squares2.append(value2**2)
print(squares2)
'''还有第3种方法，是我一直想要的类型，列表推导式'''
squares3 = [value3**2 for value3 in range(1,11)]#注意这个地方的for循环没有使用:了
print(squares3)

