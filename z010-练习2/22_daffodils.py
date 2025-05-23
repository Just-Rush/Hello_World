"""写出所有的“水仙花数”，所谓的“水仙花数”是指一个三位数其各位数字的立方和等于该数本身，例如153是“水仙花数”，因为：153 = 1**3 + 5**3 + 3**3"""


def daffodils(a):
    b = 0
    sa = str(a)
    for i in range(len((sa))):
        ia = int(sa[i])
        b += ia**3
        if a == b:
            print(a)


for j in range(101,1000):
    daffodils(j)
