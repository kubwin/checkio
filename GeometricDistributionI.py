x=input()
n=int(input())
x=x.split()
for i in range(2):
    x[i]=float(x[i])
p=x[0]/x[1]
q=1-p
B=0
for i in range(n):
   B+=q**(i)*p
B=float('{:.3f}'.format(B))
print(B)