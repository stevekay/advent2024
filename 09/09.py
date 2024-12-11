#!/usr/bin/python3

m = []
sizes = {}
bpos = {}
position = id = 0

def calcPartOne(a):
    lastused = len(a)-1
    firstfree = 0
    partone = 0
    while 1:
        while a[lastused] == -1:
            lastused -= 1

        try:
            firstfree = a.index(-1,firstfree,lastused)
        except ValueError:
            break

        a[firstfree] = a[lastused]
        a[lastused] = -1
    while lastused:
        partone += m[lastused] * lastused
        lastused -= 1
    return partone

def calcPartTwo(a,i,s,p):
    i -= 1
    c = a.index(-1)
    parttwo = 0
    while i >= 0:
        filesize = s[i]
        origpos = p[i]
        c = a.index(-1)
        ok = 0
        # start hunting for first -1
        while c < origpos and ok == 0:
            ok = 1
            # look for unused block of <filesize> size
            for l in range(0, filesize):
                if a[l+c] != -1:
                    ok = 0
                    c += l
                    break
            # if found somewhere, move it
            if ok:
                for l in range(0,filesize):
                    a[l+c] = i
                    # if all -1s from here to end of array, delete this entry
                    ggg = 1
                    for bb in range(origpos,len(a)):
                        if a[bb] != -1:
                            ggg = 0
                            break
                    if ggg == 1:
                        del a[origpos]
                    else:
                        a[origpos+l] = -1
            else:
                try:
                    c = a.index(-1,c)
                except ValueError:
                    break
        i -= 1

    c = 0
    while c < len(a):
        if a[c] != -1:
            parttwo += a[c] * c
        c += 1
    return parttwo

f = open(0,"r")
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

print(calcPartOne(m), calcPartTwo(vv,id,sizes,bpos))
