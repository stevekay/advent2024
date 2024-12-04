#!/usr/bin/python3

import fileinput

partone = 0
parttwo = 0
target='XMAS'

a=[]
rows=0

for line in fileinput.input():
    cols=len(line)-1
    a.append([])
    for col in range(0,cols):
        a[rows].append(line[col])
    rows += 1

for y in range(0,rows):
    for x in range(0,cols):
        # M S
        #  A
        # M S
        if x < cols-2 and y < rows-2 and a[y][x]=='M' and a[y][x+2]=='S' and a[y+1][x+1]=='A' and a[y+2][x]=='M' and a[y+2][x+2]=='S':
            parttwo+=1
        # S S
        #  A
        # M M
        if x < cols-2 and y < rows-2 and a[y][x]=='S' and a[y][x+2]=='S' and a[y+1][x+1]=='A' and a[y+2][x]=='M' and a[y+2][x+2]=='M':
            parttwo+=1
        # M M
        #  A
        # S S
        if x < cols-2 and y < rows-2 and a[y][x]=='M' and a[y][x+2]=='M' and a[y+1][x+1]=='A' and a[y+2][x]=='S' and a[y+2][x+2]=='S':
            parttwo+=1
        # S M
        #  A
        # S M
        if x < cols-2 and y < rows-2 and a[y][x]=='S' and a[y][x+2]=='M' and a[y+1][x+1]=='A' and a[y+2][x]=='S' and a[y+2][x+2]=='M':
            parttwo+=1

        for xd in [ -1, 0, 1 ]:
            for yd in [ -1, 0, 1]:
                found=1
                for l in range(0,len(target)):
                    if x+xd*l not in range (0, cols) or y+yd*l not in range (0, rows) or a[y+yd*l][x+xd*l] != target[l]:
                        found=0
                partone += found

print(partone,parttwo)
