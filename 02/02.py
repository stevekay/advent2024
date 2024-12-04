#!/usr/bin/python3

import fileinput

partone = 0
parttwo = 0

def testReport(x):
    increasing=0
    decreasing=0
    bigdiff=0

    for e in range(1,len(x)):
        cur = x[e]
        pre = x[e-1]
        if cur > pre:
            increasing = 1
            if cur-pre > 3:
                bigdiff = 1
        if cur < pre:
            decreasing = 1
            if pre-cur > 3:
                bigdiff = 1
        if cur == pre:
            bigdiff = 1

    if ( increasing and decreasing ) or bigdiff:
        return False
    else:
        return True

z = [[int(x) for x in line.split()] for line in fileinput.input()]

for l in z:
    if testReport(l):
        partone += 1
        parttwo += 1
    else:
        safe = 0
        for e in range(0, len(l)):
            newlist = l.copy()
            del newlist[e]
            if testReport(newlist):
                safe = 1
        parttwo += safe

print(partone, parttwo)
