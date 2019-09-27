import math
x=float(input())
a=float(input())
p=(x**a*math.e**(-x))/math.factorial(a)
p=float('{:.4f}'.format(p))
print(p)