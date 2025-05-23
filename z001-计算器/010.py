import numpy as np
x1, y1, z1, m1= map(float, input("请输入点1坐标与质量(以逗号分隔): ").split(','))
x2, y2, z2, m2= map(float, input("请输入点2坐标与质量(以逗号分隔): ").split(','))
x3, y3, z3, m3= map(float, input("请输入点3坐标与质量(以逗号分隔): ").split(','))

M = m1+m2+m3
#计算质心坐标
x0 = (x1*m1+x2*m2+x3*m3)/M
y0 = (y1*m1+y2*m2+y3*m3)/M
z0 = (z1*m1+z2*m2+z3*m3)/M
#质心坐标系下各点坐标
x11, x22, x33 = x1-x0, x2-x0, x3-x0
y11, y22, y33 = y1-y0, y2-y0, y3-y0
z11, z22, z33 = z1-z0, z2-z0, z3-z0
print(x11,y11,z11)
#计算转动惯量
Ixx = m1*(y11**2+z11**2)+m2*(y22**2+z22**2)+m3*(y33**2+z33**2)
Iyy = m1*(x11**2+z11**2)+m2*(x22**2+z22**2)+m3*(x33**2+z33**2)
Izz = m1*(y11**2+x11**2)+m2*(x22**2+y22**2)+m3*(x33**2+y33**2)
Ixy = -(m1*x1*y1+m2*x2*y2+m3*x3*y3)
Iyz = -(m1*y1*z1+m2*y2*z2+m3*y3*z3)
Ixz = -(m1*z1*x1+m2*z2*x2+m3*x3*z3)
#得到转动惯量矩阵
I = np.array([[Ixx,Ixy,Ixz],[Ixy,Iyy,Iyz],[Ixz,Ixy,Izz]])
I = I*10**-20*1.6605*10**-27
I_eigenvalues = np.linalg.eig(I)
print(I_eigenvalues)