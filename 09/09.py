#!/usr/bin/python3

f = open(0,"r")
m = []
sizes = {}
bpos = {}
partone = parttwo = 0
position = id = 0

for diskmap in f.readline().rstrip():
    if position % 2:
        m += int(diskmap) * [-1]
    else:
        bpos[id] = len(m)
        m += int(diskmap) * [id]
        sizes[id] = int(diskmap)
        id += 1
    position += 1

vv = m.copy()

# partone
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

while lastused:
    partone += m[lastused] * lastused
    lastused -= 1

# part two
id -= 1
c = vv.index(-1)
while id >= 0:
    filesize = sizes[id]
    origpos = bpos[id]
    c = vv.index(-1)
    ok = 0
    # start hunting for first -1
    while c < origpos and ok == 0:
        ok = 1
        # look for unused block of <filesize> size
        for l in range(0, filesize):
            if vv[l+c] != -1:
                ok = 0
                c += l
                break

        # if found somewhere, move it
        if ok:
            for l in range(0,filesize):
                vv[l+c] = id
                vv[l+origpos] = -1
        else:
            c = vv.index(-1,c+1)
    id -= 1

c = 0
while c < len(vv):
    if vv[c] != -1:
        parttwo += vv[c] * c
    c += 1

print(partone,parttwo)
