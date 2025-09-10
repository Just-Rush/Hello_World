# 尝试调用 Random ，在二维空间定义一个正方形区域﹣1< x ≤1,-1≤ y ≤1用 Random 产生10万个位于正方形区域内的点，并计算这些点落在以（0,0）为圆心、半径为1的圆内的比例。
import random
import time
st = time.time()

a = 0
for i in range(100000):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        a += 1
ratio = a/100000
print(ratio)
end = time.time()
print(end - st)

"""random()：生成一个[0.0, 1.0)之间的随机浮点数。
randint(a, b)：生成一个[a, b]之间的随机整数。
randrange([start,] stop[, step])：生成一个[start, stop)之间以step为步长的随机整数。
choice(seq)：从非空序列seq中随机选择一个元素。
shuffle(list)：将list中的元素随机打乱。
sample(population, k)：从population中随机选择k个不重复的元素。
uniform(a, b)：生成一个[a, b]之间的随机浮点数。
normalvariate(mu, sigma)：生成一个符合正态分布的随机数，mu是均值，sigma是标准差      
b = random.random()
print(b)    
原文链接：https://blog.csdn.net/qq_53810226/article/details/138687123"""

