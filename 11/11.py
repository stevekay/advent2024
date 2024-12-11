#!/usr/bin/python3

s=open(0,"r").readline().rstrip().split(' ')
a={}
for _ in s:a[_]=(a.get(_)or 0)+1
c=0
while c<75:
 z={}
 for p in a.keys():
  if len(str(p))%2:
   k=1if p=='0'else str(int(p)*2024)
   z[k]=(z.get(k)or 0)+a[p]
  else:
   for d in(int(p[:len(p)//2]),int(p[len(p)//2:])):
    z[str(d)]=(z.get(str(d))or 0)+a[p]
 c+=1
 a=z.copy()
 if c in[25,75]:print(sum(a.values()))
