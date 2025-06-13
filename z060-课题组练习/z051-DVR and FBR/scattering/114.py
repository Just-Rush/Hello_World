import numpy as np
from scipy import integrate

pi = np.pi
hbar = 1
me = 1
k = 1
ene = 1

# 定义ψ（0）
def psi_0(x):
    k_wavevector = 1  # 平面波的波矢量
    psi0 = np.exp(1j * k_wavevector * x)  # 平面波形式
    return psi0

# 定义Φn
def phi_n(n, b, a, x):
    c = b - a
    phin = np.sqrt(2 / c) * np.sin((n + 1) * pi * x / c)
    return phin

# 定义Cn(0)
def cn1(n, b, a):
    temp = lambda x: np.conjugate(phi_n(n, b, a, x)) * psi_0(x)  # 取共轭
    cn, err = integrate.quad(temp, a, b, complex_func=True)
    return cn

###############################################################################################

# 定义e（εn/2），εn为一维势箱的能级
def e_epsilon_n(n, b, a, t):
    epsilonn = n**2 * hbar**2 * pi**2 / 2 / (b - a)**2 / me
    e_epsn = np.exp(-1j * epsilonn * t / 2)
    return e_epsn

# 定义xl，格点
def xl(n, b, a):
    return np.linspace(a, b, n)

# 定义ε（vxl）
def e_vxl(xl, t):
    vxl = 0.5 * k * xl**2
    evxl = np.exp(-1j * vxl * t)
    return evxl

# 定义Bnl，表象变换矩阵
def bnl(n):
    Bnl_matrix = np.zeros((n, n), dtype=complex)
    for i in range(n):
        for j in range(n):
            Bnl_matrix[i, j] = np.sqrt(2 / n) * np.sin((i + 1) * (j + 1) * pi / (n + 1))
    return Bnl_matrix

# 计算Cn'''，最终的系数矩阵
def cn_4(n, b, a, dt, total_time):
    time_steps = int(total_time / dt)
    cn4_list = []
    cn_initial = [cn1(i + 1, b, a) for i in range(n)]
    Bnl_matrix = bnl(n)
    for _ in range(time_steps):
        cn_current = []
        for i in range(n):
            e_epsn_squared = e_epsilon_n(i + 1, b, a, dt / 2)**2
            evxl_value = e_vxl(xl(n, b, a), dt)[i]
            bnlsquared = Bnl_matrix[:, i]**2
            cn_new = cn_initial[i] * e_epsn_squared * bnlsquared * evxl_value
            cn_current.append(cn_new)
        cn4_list.append(np.array(cn_current))
        cn_initial = cn_current
    return np.array(cn4_list)

# 计算ψ（E）
def psi_e(n, b, a, dt, total_time):
    xl_values = xl(n, b, a)
    cn4_values = cn_4(n, b, a, dt, total_time)
    psi_e_values = np.zeros_like(xl_values, dtype=complex)
    for t_step in range(len(cn4_values)):
        for i in range(n):
            psi_e_values += cn4_values[t_step][i] * phi_n(i + 1, b, a, xl_values)
    return psi_e_values

# 参数设置
n = 8
b = 5
a = -5
dt = 0.01
total_time = 3

# 计算并打印结果
psi_e_result = psi_e(n, b, a, dt, total_time)
print(psi_e_result)



