#!/usr/bin/python3

import fileinput

grid=[]
antennas={}
antinodes_partone = 0
antinodes_parttwo = 0

for line in open(0).readlines():
    grid.append(list(line.strip()))

for y in range(len(grid)):
    for x in range(len(grid[y])):
        c = grid[y][x];
        if c.isalnum():
            if not c in antennas:
                antennas[c] = []
            antennas[c].append([x,y])
    maxX = x
maxY = y

for a in antennas:
    signals=antennas[a]
    for position in range(len(signals)):
        (thisX,thisY)=signals[position]
        for newposition in set(range(len(signals))) - {position}:
            (newX,newY)=signals[newposition]
            diffX = newX-thisX
            diffY = newY-thisY
            antiX = newX + diffX
            antiY = newY + diffY

            while antiY >= 0 and antiY <= maxY and antiX >= 0 and antiX <= maxX:
                grid[antiY][antiX]='#'
                antiY += diffY
                antiX += diffX

for row in range(len(grid)):
    antinodes_partone += grid[row].count('#')
    antinodes_parttwo += len([i for i in grid[row] if i != '.'])

print(antinodes_partone,antinodes_parttwo)
