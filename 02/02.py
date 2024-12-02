#!/usr/bin/python3

import fileinput

tot = 0

for line in fileinput.input():
    line=line.strip()

    increase_found = 0
    decrease_found = 0
    same_found = 0
    big_diff_found = 0

    for e in range(1,line.count(' ')+1):
        cur = int(line.split(' ')[e])
        pre = int(line.split(' ')[e-1])
        if cur > pre:
            increase_found = 1
        if cur < pre:
            decrease_found = 1
        if cur == pre:
            same_found = 1
        if abs(cur - pre) > 3:
            big_diff_found = 1
    if (increase_found and decrease_found) or same_found or big_diff_found:
        pass
    else:
        tot += 1

print(tot)
