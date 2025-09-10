import math
import matplotlib.pyplot as plt
import numpy as np

pi = math.pi
hba = 1
me = 1
kc = 1


def hamilton(n, b, a):
    hm = np.zeros((n, n))
    for i in range(1, n + 1):
        t = hba ** 2 / (2 * me) * (i * pi / (b - a)) ** 2
        for j in range(1, n + 1):
            wl = (b - a) / (n + 1)
            vij = 0
            for k in range(1, n + 1):
                xl = a + (k * (b - a) / (n + 1))
                phim = math.sqrt(2 / (b - a)) * math.sin(i * pi * (xl - a) / (b - a))
                phin = math.sqrt(2 / (b - a)) * math.sin(j * pi * (xl - a) / (b - a))
                vij += wl * phim * 0.5 * kc * xl ** 2 * phin

            if i == j:
                hm[i - 1, j - 1] = t + vij
            else:
                hm[i - 1, j - 1] = vij

    eigenvalue, eigenvector = np.linalg.eig(hm)

    eigenvalue_sorted_indexes = np.argsort(eigenvalue)
    vals = eigenvalue[eigenvalue_sorted_indexes]
    vecs = eigenvector[:, eigenvalue_sorted_indexes]

    print(vals, vecs)

    # 画图
    x = np.linspace(a, b, 1000)
    for k in range(min(3, n)):  # 画图数量
        psi_k = []
        for xi in x:
            sum_psi = 0
            for m in range(n):
                phi_m = math.sqrt(2 / (b - a)) * math.sin((m + 1) * pi * (xi - a) / (b - a))
                sum_psi += vecs[m, k] * phi_m
            psi_k.append(sum_psi)

        plt.figure(figsize=(10, 8))
        plt.plot(x, psi_k, label=f'n={k}')
        plt.xlabel('x')
        plt.ylabel('ψ(x)')
        plt.title(f'wavefunction for n={k}')
        plt.legend()
        plt.grid(True)
        plt.show()


hamilton(100, 10, -10)






