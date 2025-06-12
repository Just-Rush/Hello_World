import math
import numpy as np
from scipy import integrate
import matplotlib as plt

pi = np.pi
hbar = 1
me = 1
k = 1
ene =1

  # 定义ψ（0）
def psi_0(x):
    psi0 = np.sin(x)  # 应该定义为平面波！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    return psi0

  # 定义Φn
def phi_n(n,b,a,x):
    c = b-a
    phin = np.sqrt(2/c)*np.sin((n+1)*pi*x/c)
    return phin

  # 定义Cn(0)
def cn1(n,b,a):
    temp = lambda x:phi_n(i,b,a,x)*psi_0(x)  # 此处需要取共轭！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    cn_1 = []
    for i in range(n):
        cn, err = integrate.quad(temp,a,b)
        cn_1.append(cn)
    return np.array(cn_1)

###############################################################################################

  # 定义e（εn/2），εn为一维势箱的能级
def e_episilon_n(n,b,a,t):
    epsilonn = np.array([i**2*hbar**2*pi**2/2/(b-a)/me for i in range(1,n+1)])
    e_epsn = np.exp(-1j*epsilonn*t/2)
    return e_epsn

  # 定义xl，格点
def xl(n,b,a):
    return np.array([a+(l+1)*(b-a)/(n+1) for l in range(n)])

  # 定义ε（vxl）
def e_vxl(n,b,a,t):
    vxl = 0.5*k*xl(n,b,a)**2
    evxl = np.exp(-1j*vxl*t)
    return evxl

  # 定义Bnl，表象变换矩阵
def bnl(n):
    return np.array([np.sqrt(2/(n+1))*np.sin(n*(l+1)*pi/(n+1)) for l in range(n)])

  # 计算Cn'''，最终的系数矩阵
def cn_4(n,b,a,t):
    cn4 = cn1(n,b,a)*e_episilon_n(n,b,a,t)**2*bnl(n)**2*e_vxl(n,b,a,t)
    return cn4

  # 计算a(E)
def ae(n,b,a):
    aee = lambda x:psi_0(x) * np.sqrt(2/(b-a))*np.sin((n+1)*pi*x/(b-a)) #  此处是ψ（E），这个表达式肯定不对
    return aee

  # 计算ψ（E）
def psi_e(n,b,a,t):
    constant_a = 1/2*pi/ae(n,b,a)
    psie_no_e = 0
    for i in range(1,t+1):
        for j in range(n):
            psie_no_canstant_a = np.exp(1j*ene)*cn_4(n,b,a,i)*phi_n(n,b,a,xl(n,b,a))
            psie_no_e += psie_no_canstant_a
    psie = psie_no_e*constant_a
    print(psie)
    return psie


psi_e(8,5,-5,3)