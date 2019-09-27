import sys

q=''
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
for i in range(n):
    q+=str(arr[n-1-i])+' '
print(str(q))