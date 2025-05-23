from sympy import *
x = symbols('x')
print(integrate(x**2 + exp(x) + 1, (x, 0, 1)))