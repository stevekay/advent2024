#!/usr/bin/python3

import fileinput

listone, listtwo = [], []

for line in fileinput.input():
    listone.append(int(line.split(None)[0]))
    listtwo.append(int(line.split(None)[1]))

listone.sort()
listtwo.sort()

partone = parttwo = 0
for a in range(len(listone)):
    partone += abs(listone[a] - listtwo[a])
    parttwo += listtwo.count(listone[a]) * listone[a]

print(partone,parttwo)
