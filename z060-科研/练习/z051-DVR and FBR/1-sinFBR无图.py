import math
import numpy as np
import time


pi = math.pi
hba = 1
me = 1
kc = 1


def hamilton(n, b, a):  # n是psi的基函数的个数，也即矩阵的宽度；b,a表示势阱的长度;
    hm = np.zeros((n, n))
    for i in range(1, n+1):

        t = hba**2 / (2 * me) * (i * pi / (b - a)) ** 2  # 计算动能项

        for j in range(1, n+1):

            wl = (b-a)/(n+1)
            vij = 0
            for k in range(1, n+1):  # 计算势能项
                xl = a + (k*(b - a)/(n + 1))
                phim = math.sqrt(2/(b-a))*math.sin(i*pi*(xl-a)/(b-a))
                phin = math.sqrt(2 / (b - a)) * math.sin(j * pi * (xl - a) / (b - a))
                vij += wl*phim*0.5*kc*xl**2*phin

            if i == j:
                hm[i-1, j-1] = t + vij
            else:
                hm[i-1, j-1] = vij

  # 对角化哈密顿矩阵
    eigenvalue, eigenvector = np.linalg.eig(hm)

    eigenvalue_sorted_indexes = np.argsort(eigenvalue)  # argsort 接受一个数组作为输入，并返回一个索引数组，该索引数组表示输入数组排序后的顺序。
    vals = eigenvalue[eigenvalue_sorted_indexes]  # 与直接使用vvv = np.sort(eigenvalue)效果相同，但后续还有对应本征向量，所以排序其索引更好
    vecs = eigenvector[:, eigenvalue_sorted_indexes]
    print(vals,vecs)

hamilton(100, 10, -10)
