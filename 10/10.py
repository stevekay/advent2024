#!/usr/bin/python3

g, s, p1, p2=[], {}, 0, 0

def f(a,x,y,v):
    global s, p2
    for (i, j) in ( [x+1,y], [x-1,y], [x,y+1], [x,y-1] ):
        if len(a[x]) > i >= 0 <= j < len(a) and a[j][i] == str(v):
            if v == 9:
                s[i,j] = 1
                p2 += 1
            else: f(a, i, j, v+1)

for _ in open(0).readlines(): g.append(list(_.strip()))

for y, _ in enumerate(g):
    for x, _ in enumerate(g[y]):
        if g[y][x] == '0':
            s = {}
            f(g, x, y, 1)
            p1 += len(s)

print(p1,p2)
