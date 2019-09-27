'''n=int(input())
a=input()
b=input()'''
n=5
a='10 40 30 50 20'
b='1 2 3 4 5'
x=a.split()
w=b.split()
sum=0
d=0
for i in range(n):
    sum+=float(x[i])*float(w[i])
    d+=float(w[i])
m=sum/d
m=float('{:.1f}'.format(m))
print(m)