n=int(input())
a = []

s1=''
s2=''
for i in range(n):
    a.append(input())
for i in range(len(a)):
   s1=''
   s2=''
   for j in range(len(a[i])):
        if j%2==0:
            s1+=a[i][j]
        else:
            s2+=a[i][j]
   print(s1, s2)
