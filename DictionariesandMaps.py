n=int(input())
g={}
for i in range(n):
      s=input().split()
      g.update({s[0]:s[1]})
s=[]
for i in range(n):
      s.append(input())
for key in s:
      if key in g:
          print(key+ "="+ g.get(key))
      else:
            print("Not found")
