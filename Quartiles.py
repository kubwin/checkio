n = int(input())
x = input()
y = input()


y1=y.split()
X = x.split()
x1 = []
for i in range(n):
    X[i] = int(X[i])
for i in range(n):
    y1[i] = int(y1[i])
for i in range(n):
    for j in range(y1[i]):
        x1.append(X[i])

x1 = sorted(x1)
print(x1)
n=len(x1)
Srednee = divmod(n, 2)
if Srednee[1] == 0:
    Q2 = (x1[Srednee[0] - 1] + x1[Srednee[0]]) / 2
else:
    Q2 = x1[Srednee[0]]
    x1.pop(Srednee[0])

x2=x1[0:(Srednee[0])]
SredneeRight = divmod(Srednee[0], 2)
if SredneeRight[1] == 0:
    Q1 = (x2[SredneeRight[0] - 1] + x2[SredneeRight[0]]) / 2
else:
    Q1 = x2[SredneeRight[0]]



x3=x1[(Srednee[0]):n]
SredneeRight = divmod(len(x3), 2)
if SredneeRight[1] == 0:
    Q3 = (x3[SredneeRight[0] - 1] + x3[SredneeRight[0]]) / 2
else:
    Q3 = x3[SredneeRight[0]]
m=Q3-Q1
m=float('{:.1f}'.format(m))
print(m)

