import math

def Bin(a, p, n):
    return (math.factorial(n) / (math.factorial(a) * math.factorial(n - a))) * p ** a * (1 - p) ** (n-a)

x=input()
x=x.split()
for i in range(2):
    x[i]=float(x[i])
p=x[0]/(x[0]+x[1])
#p=float('{:.3f}'.format(p))
B=0
for i in range(3,7):
    B+=Bin(i,p,6)

B=float('{:.3f}'.format(B))
print(B)