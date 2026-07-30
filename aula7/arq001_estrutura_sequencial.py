"""
Considera a equação quadratica x² +2x -3 = 0.
"""

a = 1
b = 2
c = -3
delta = (b**2) - (4*a*c)
x1 = (-b + (delta**(1/2))) / (2*a)
x2 = (-b - (delta**(1/2))) / (2*a)
print(delta)
print("os valores de X são: ", x1, " e ", x2,".")


