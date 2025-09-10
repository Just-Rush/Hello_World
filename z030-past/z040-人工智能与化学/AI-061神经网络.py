import numpy as np


x = np.array([[7],[5],[6]])
print(x)
w1 = np.array([[3, 2, 0],[1, 4, 2],[0,2,-5]])
print(w1)
w2 = np.array([1,-0.5,2])  # 这是取了转置了，本来是个列向量。
z1 = np.dot(w1.T,x).flatten()
print(f'第一层输出{z1}')
z2 = np.dot(w2,z1)  # 注意是w转置点乘x，或是x点乘w不转置。
print(f'第二层输出{z2}')

#附加激活函数relu
print('若在每层后增加relu激活函数，则分别得到结果')
rule_z1 = np.maximum(0,z1)
print(rule_z1)
temp_z2 = np.dot(rule_z1,w2)
rule_z2 = np.maximum(0,temp_z2)
print(rule_z2)
