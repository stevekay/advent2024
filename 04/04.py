#!/usr/bin/python3

import fileinput
import re

partone = parttwo = 0
target='XMAS'
a=[]

for b in open(0).readlines():
    a.append(list(b.strip()))

for y in range(0,len(a)):
    for x in range(0,len(a[0])):
        if x < len(a[0])-1 and y and y < len(a)-1:
            parttwo += bool(re.match(r'^(MSAMS|SSAMM|MMASS|SMASM)$', \
              a[y-1][x-1] + a[y-1][x+1] + a[y][x] + \
              a[y+1][x-1] + a[y+1][x+1]))

        for xd in [ -1, 0, 1 ]:
            for yd in [ -1, 0, 1]:
                found = 1
                for l in range(0, len(target)):
                    if x+xd*l not in range (0, len(a[0])) or \
                       y+yd*l not in range (0, len(a)) or \
                       a[y+yd*l][x+xd*l] != target[l]:
                        found = 0
                partone += found

print(partone, parttwo)
