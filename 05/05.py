#!/usr/bin/python3

import fileinput
import pprint
import random

partone = 0
parttwo = 0
before = {}

def checkPage(l,r):
    goodline = 1
    sofar = []
    tot = 0
    for t in line.split(','):
        if t in before:
            for p in r[t]:
                if p in sofar:
                    goodline = 0
                    baddigit = t
        sofar.append(t)
    if goodline:
        tot += int(updateline[ int(len(updateline)/2) ])
    else:
        return(-1,baddigit)
    return(tot,0)

gotallorders = 0
for line in fileinput.input():
    line = line.rstrip('\n')
    if "|" in line:
        (earlypage,latepage)=line.split("|")

        if earlypage in before:
            before[earlypage].append(latepage)
        else:
            before[earlypage]=[]
            before[earlypage].append(latepage)

    if "," in line:
        updateline = line.split(",")
        (orderok, baddigit) = checkPage(updateline,before)
        if orderok == -1:
            badline = 1
            while badline == 1:
                for c in before[baddigit]:
                    if c in updateline:
                        a1 = updateline.index(baddigit)
                        if c not in updateline[a1+1:]:
                            #print("moving",baddigit," to different position")
                            updateline.remove(baddigit)
                            a2=updateline.index(c)
                            updateline.insert(a2,baddigit)
                (orderok, baddigit) = checkPage(updateline,before)
                if orderok == -1:
                    badline = 0
            #print("mid=",updateline[ int(len(updateline)/2) ])
            print(line,"becomes",",".join(updateline))

        else:
            partone += orderok

print("breaks rule:")
print("97,13,75,29,47 becomes 97,75,47,29,13")
#print(partone,parttwo)
