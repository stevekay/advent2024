#!/usr/bin/python3

import fileinput

grid=[]
antennas={}
       
def drawGrid(g):
    a = '   ' + ''.join(str(i) for i in range(len(grid[0])))
#    print(a)
    antinodes = 0
    for row in range(len(grid)):
        antinodes += g[row].count('#')
#        print(f'0{row}|' + ''.join(g[row]) + f'|0{row}')
#    print(a)
    print("Antinodes=",antinodes)

for line in open(0).readlines():
    grid.append(list(line.strip()))
#print(grid)

drawGrid(grid)

for y in range(len(grid)):
    for x in range(len(grid[y])):
        c = grid[y][x];
        if c.isalnum():
            print(c,"found at x=",x,"y=",y)
            if not c in antennas:
                antennas[c] = []
            antennas[c].append([x,y])
    maxX = x
maxY = y

print(antennas)
#print("maxX=",maxX,"maxY=",maxY)

for a in antennas:
#    print("antenna label:",a," : ",antennas[a])
    l=antennas[a]
    for p in range(0,len(l)):
        (thisX,thisY)=l[p]
#        print(" -> antenna ",p,"at x=",thisX,",y=",thisY)
        for q in range(0,len(l)):
            if p != q:
                (newX,newY)=l[q]
                diffX = newX-thisX
                diffY = newY-thisY
                antiX = newX + diffX
                antiY = newY + diffY
#                print("  -> comparing with ",q,"at",newX,",",newY,"diffX=",diffX,"diffY=",diffY,"so antinode at x=",antiX,"y=",antiY)
                if antiY >= 0 and antiY <= maxY and antiX >= 0 and antiX <= maxX:
                    grid[antiY][antiX]='#'
drawGrid(grid)

