import math
import numpy as np
from scipy import integrate

pi = np.pi
hbar = 1
me = 1
k = 1

# 定义ψ（0）
def psi_0(x):
    return np.cos(x)

# 定义Φn
def phi_n(n, b, a, x):
    c = b - a
    phin = np.sqrt(2 / c) * np.sin((n + 1) * pi * x / c)
    return phin

# 定义Cn(0)
def cn1(n, b, a):
    results = []
    for i in range(n):
        aa = lambda x: phi_n(i + 1, b, a, x) * psi_0(x)
        cn_1, _ = integrate.quad(aa, a, b)
        results.append(cn_1)
    return np.array(results)

print(cn1(3, 2, -2))



