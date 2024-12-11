#!/usr/bin/python3

import fileinput

partone = 0
parttwo = 0
after = {}

for line in fileinput.input():
    line = line.rstrip('\n')
    if "|" in line:
        (earlypage,latepage)=line.split("|")

        if earlypage in after:
            after[earlypage].append(latepage)
        else:
            after[earlypage]=[]
            after[earlypage].append(latepage)

    if "," in line:
        updateline = line.split(",")
        sofar = []
        goodline = 1
        for thispage in updateline:
            if thispage in after:
                for p in after[thispage]:
                    if p in sofar:
                        goodline = 0
            sofar.append(thispage)
        if goodline:
            partone += int(updateline[ int(len(updateline)/2) ])
        else:
            print("bad line, so need to reorder")

print(partone,parttwo)
