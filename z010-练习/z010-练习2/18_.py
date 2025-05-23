"""如果整数A的全部因子（包括1，不包括A本身）之和等于B；且整数B的全部因子（包括1，不包括B本身）之和等于A，则将整数A和B称为亲密数。求3000以内的全部亲密数。"""
"""其实本质跟17一样，是求因子；且这个定义就解释得比17清楚"""

for i in range(1, 30):
    a = 0
    l1 = []
    for ia in range(1, int(i / 2 + 1)):  # 计算e的全部因子的和
        if i % ia == 0:
            a += ia
    l1.append(a)
    for j in range(1, 30):
        if l1[i] == j and l1[j] == i:
            print(i, j)


