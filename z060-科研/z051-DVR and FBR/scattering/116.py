import math
import numpy as np
from scipy import integrate
import matplotlib as plt


pi = np.pi
hbar = 1
me = 1
k = 1

  # 定义ψ（0）
def psi_0(x):
    psi0 = np.sin(x)
    return psi0

  # 定义Φn
def phi_n(n,b,a,x):
    c = b-a
    phin = np.sqrt(2/c)*np.sin((n+1)*pi*x/c)
    return phin

  # 定义Cn(0)
def cn1(n,b,a):
    temp = lambda x: phi_n(i, b, a, x) * psi_0(x)

    cn_1 = []
    for i in range(n):

        cn, err = integrate.quad(temp,a,b)
        cn_1.append(cn)
    return np.array(cn_1)

print(cn1(2,1,-1))