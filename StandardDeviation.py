'''
n=input()
x=int(input())
'''
n=5
Y='10 40 30 50 20'
sum = 0
Y1 = Y.split()
for i in range(n):
    Y1[i] = int(Y1[i])
for i in range(n):
    sum += Y1[i]
u = sum / n

x=0
for i in range(n):
    x+=(Y1[i]-u)**2
x=(x/n)**(0.5)
x=float('{:.1f}'.format(x))
print(x)