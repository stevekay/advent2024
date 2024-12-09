#!/usr/bin/python3

f = open(0,"r")
m = []

position = id = 0
for diskmap in f.readline().rstrip():
    if position % 2:
        m += int(diskmap) * [-1]
    else:
        m += int(diskmap) * [id]
        id += 1
    position += 1

lastused = len(m)-1
firstfree = 0

while 1:
    while m[lastused] == -1:
        lastused -= 1

    try:
        firstfree = m.index(-1,firstfree,lastused)
    except ValueError:
        break

    m[firstfree], m[lastused] = m[lastused], -1

partone = 0
while lastused:
    partone += m[lastused] * lastused
    lastused -= 1
print(partone)

