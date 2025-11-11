import numpy as np
import math

def cal_iin(n):
    if n == 0:
        return 1 - np.exp(-1)
    else:
        iin = -np.exp(-1) + (n+1) * cal_iin(n-1)
        return iin

def other(n):
    n = n+1
    if n == 1:
        return 1-np.exp(-1)
    else:
        result = math.factorial(n) - np.exp(-1) * (sum(math.factorial(n) // math.factorial(n - k) for k in range(0,n)))

        return result
for i in range(0, 11):
    
    print(cal_iin(i))
    print(other(i))