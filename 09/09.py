#!/usr/bin/python3

f = open(0,"r")
pos = id = firstfree = partone = c = z = 0
m = []
for c in f.readline().rstrip():
    if pos % 2 == 0:
        m += int(c) * [id]
        id += 1
    else:
        m += int(c) * [-1]
    pos += 1

lastused=len(m)-1

while 1:
    while m[lastused] == -1:
        lastused -= 1

    try:
        firstfree = m.index(-1,firstfree,lastused)
    except ValueError:
        break

    m[firstfree] = m[lastused]
    m[lastused] = -1

while m[z] != -1:
    partone += z * m[z]
    z += 1

print(partone)
