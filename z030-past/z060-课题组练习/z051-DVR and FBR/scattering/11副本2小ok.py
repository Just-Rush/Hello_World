import math
import numpy as np
from scipy import integrate

pi = np.pi
hbar = 1
me = 1
k = 1

# 定义ψ（0）
def psi_0(x):
    return np.sin(x)

# 定义Φn
def phi_n(n, b, a, x):
    c = b - a
    phin = np.sqrt(2 / c) * np.sin((n + 1) * pi * x / c)
    return phin

# 定义Cn(0)
def cn1(n, b, a):
    cn_1 = []
    for i in range(n):
        temp = lambda x: phi_n(i + 1, b, a, x) * psi_0(x)
        cn, err = integrate.quad(temp, a, b)
        cn_1.append(cn)
    return np.array(cn_1)

####################################################

# 定义e（εn/2），εn为一维势箱的能级
def e_episilon_n(n, b, a, t):
    epsilonn = np.array([i**2 * hbar**2 * pi**2 / 2 / (b - a) / me for i in range(1, n + 1)])
    e_epsn = np.exp(-1j * epsilonn * t / 2)
    return e_epsn

# 定义xl，格点
def xl(n, b, a):
    return np.array([a + (l + 1) * (b - a) / (n + 1) for l in range(n)])

# 定义ε（vxl）
def e_vxl(n, b, a, t):
    vxl = 0.5 * k * xl(n, b, a)**2
    evxl = np.exp(-1j * vxl * t)
    return evxl

# 定义Bnl，表象变换矩阵
def bnl(n):
    return np.array([np.sqrt(2 / (n + 1)) * np.sin(n * (l + 1) * pi / (n + 1)) for l in range(n)])

# 计算Cn'''，最终的系数矩阵
def cn_4(n, b, a, t):
    cn4 = cn1(n, b, a) * e_episilon_n(n, b, a, t)**2 * bnl(n)**2 * e_vxl(n, b, a, t)
    return cn4

n = 5
b = 2
a = -2
t = 1

cn4_result = cn_4(n, b, a, t)
xl_result = xl(n, b, a)
e_epsilon_n_result = e_episilon_n(n, b, a, t)
e_vxl_result = e_vxl(n, b, a, t)
bnl_result = bnl(n)

print(f"Cn''':\n{cn4_result}\n")
print(f"xl:\n{xl_result}\n")
print(f"e(εn/2):\n{e_epsilon_n_result}\n")
print(f"ε(vxl):\n{e_vxl_result}\n")
print(f"bnl:\n{bnl_result}\n")
print(f"cn1:\n{cn1(n,b,a)}\n")



