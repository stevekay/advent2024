#!/usr/bin/python3

import fileinput
import re

partone = parttwo = 0
target='XMAS'

a=[]

for b in open(0).readlines():
    a.append(list(b.strip()))

cols=len(a[0])

for y in range(0,len(a)):
    for x in range(0,cols):
        if x < cols-1 and y > 0 and y < len(a)-1 and a[y][x]=='A':
            if re.match(r'^(MSMS|SSMM|MMSS|SMSM)$', a[y-1][x-1] + a[y-1][x+1] + a[y+1][x-1] + a[y+1][x+1]):
                parttwo += 1

        for xd in [ -1, 0, 1 ]:
            for yd in [ -1, 0, 1]:
                found = 1
                for l in range(0,len(target)):
                    if x+xd*l not in range (0, cols) or y+yd*l not in range (0, len(a)) or a[y+yd*l][x+xd*l] != target[l]:
                        found = 0
                partone += found

print(partone, parttwo)
