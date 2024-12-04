#!/usr/bin/python3

import fileinput
import re

partone = 0
parttwo = 0
target='XMAS'

a=[]
rows=0

for line in fileinput.input():
    cols = len(line)-1
    a.append([])
    for col in range(0,cols):
        a[rows].append(line[col])
    rows += 1

for y in range(0,rows):
    for x in range(0,cols):
        if x < cols-1 and y > 0 and y < rows-1 and a[y][x]=='A':
            if re.match(r'^(MSMS|SSMM|MMSS|SMSM)$', a[y-1][x-1] + a[y-1][x+1] + a[y+1][x-1] + a[y+1][x+1]):
                parttwo += 1

        for xd in [ -1, 0, 1 ]:
            for yd in [ -1, 0, 1]:
                found = 1
                for l in range(0,len(target)):
                    if x+xd*l not in range (0, cols) or y+yd*l not in range (0, rows) or a[y+yd*l][x+xd*l] != target[l]:
                        found = 0
                partone += found

print(partone, parttwo)
