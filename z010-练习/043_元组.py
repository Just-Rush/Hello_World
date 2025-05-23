#练习4.13
a = ('a','b','c','d','e')
for b in a:
    print(b)
a = ('a','b','c','f','g')
print(a)

'''
总结：
列表 = [,,,]
    append,insert
    remove,pop,popped,del
    sort,sorted,reverse
len(A)
for 循环
    for A in B:
range函数
    list(range()),创建数值列表
    min,max,sum
    列表推导式
切片
    [:]
    创建的是（互相独立的）列表副本，赋值是指向同一个列表
元组
    (,)
    元组变量可以重新定义
代码格式
    缩进时往往缩进4个空格（正好2个中文字符）
    行长不超过79，，注释不超过72
    不同部分分开可使用空行，往往只用1个空行    #python不关心垂直间距，只关心水平缩进，（相同缩进程度为一个层次，并不是一定要4空格，只是约定如此，这样也美观一些（美观是不是就是可读性）
    
'''