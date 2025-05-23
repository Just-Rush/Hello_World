import math
import numpy as np
import matplotlib.pyplot as plt

pi = math.pi
hbar = 1
me = 1
kc = 1


# 获取势能矩阵矩阵元
def get_v_value(n, b, a):  # n是psi的基函数的个数，也即矩阵的宽度,也是格点数；b,a表示势阱的长度
    vxl_list = []
    for l in range(1, 1 + n):
        xl = a + l * (b - a) / (n + 1)
        vxl = 0.5 * kc * xl ** 2
        vxl_list.append(vxl)
    return vxl_list


# 获取势能矩阵
def get_v_matrix(n, vxl_list):
    v_mat = np.zeros((n, n))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                v_mat[i - 1, j - 1] = vxl_list[i - 1]
    return v_mat


# 获取动能矩阵
def get_t_matrix(n, b, a):
    t_matrix = np.zeros((n, n))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                t_matrix[i - 1, j - 1] = 0.25 / me * pi ** 2 / (b - a) ** 2 * (-1) ** (i - j) * (
                        1 / (math.sin(pi * (i - j) / 2 / (n + 1)) ** 2) -
                        1 / (math.sin(pi * (i + j) / 2 / (n + 1)) ** 2))
            else:
                t_matrix[i - 1, j - 1] = 0.25 / me * pi ** 2 / (b - a) ** 2 * (
                        (2 * (n + 1) ** 2 + 1) / 3 -
                        (1 / (math.sin(pi * i / (n + 1))**2)))
    return t_matrix


def Bml(m,n,i):
    bml = np.sqrt(2/(n+1))*np.sin(m*i*pi/(n+1))
    return bml

def wl(n,b,a):
    wll = (b-a)/(n+1)
    return wll



# 获取哈密顿矩阵并求解本征值本征向量
def dvr_solve(n, b, a):
    get_v_value(n,b,a)
    h_matrix = get_t_matrix(n, b, a) + get_v_matrix(n, get_v_value(n, b, a))  # !!!

    eigenvalue, eigenvector = np.linalg.eig(h_matrix)
    eigenvalue_sorted_indices = np.argsort(eigenvalue)
    lamb = eigenvalue[eigenvalue_sorted_indices]
    vecs = eigenvector[:, eigenvalue_sorted_indices]

    print("本征值:\n", lamb)
    # print("本征矢:\n", vecs)

    # 显示波函数
    # xl_list = []
    # for ii in range(1,n+1):
    #     xll = a +ii*(b-a)/(n+1)
    #     xl_list.append(xll)
    #     xx = np.array(xl_list)
    x = np.linspace(a, b, n)
    psi_list =[]
    plt.figure(figsize=(10, 8))
    for k in range(min(3, n)):  # 显示图像个数
        psi_k = vecs[:, k]
        # psi_list.append(psi_k)

        plt.plot(x, psi_k, label=f'n={k}')
    plt.xlabel('x')
    plt.ylabel('ψ(x)')
    plt.title(f'wavefunction for dvr')
    plt.legend()
    plt.grid(True)
    plt.show()


dvr_solve(160, 10, -10)






