import math

def Bin(a, p, n):
    return (math.factorial(n) / (math.factorial(a) * math.factorial(n - a))) * p ** a * (1 - p) ** (n-a)

x=input()
x=x.split()
for i in range(2):
    x[i]=float(x[i])
p=x[0]/100
q=1-p
n=x[1]
B=0
for i in range(3):
    B+=Bin(i,p,n)

B=float('{:.3f}'.format(B))
print(B)
B=0
for i in range(2,11):
    B+=Bin(i,p,n)
B=float('{:.3f}'.format(B))
print(B)
