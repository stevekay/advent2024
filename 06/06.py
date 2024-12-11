#!/usr/bin/python3

import fileinput

grid=[]
been={}
directionInfo = { 'N': { 'X':  0, 'Y': -1, 'NEXT': 'E' }, 
                  'E': { 'X': +1, 'Y':  0, 'NEXT': 'S' },
                  'S': { 'X':  0, 'Y': +1, 'NEXT': 'W' },
                  'W': { 'X': -1, 'Y':  0, 'NEXT': 'N' } }
robotDir='N'
        
for line in open(0).readlines():
    grid.append(list(line.strip()))

for rownum in range(0,len(grid)):
    if '^' in grid[rownum]:
        robotY=rownum
        robotX=grid[rownum].index("^")

while(1):
    diffX = directionInfo[robotDir]['X']
    diffY = directionInfo[robotDir]['Y']

    while grid[robotY+diffY][robotX+diffX] != '#':
        been[robotX,robotY]=1
        robotY+=diffY
        robotX+=diffX
        if robotY == len(grid)-1 or robotY == 0 or robotX == len(grid[0])-1 or robotX == 0:
            print(len(been)+1)
            exit()

    robotDir = directionInfo[robotDir]['NEXT']
