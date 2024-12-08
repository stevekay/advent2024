#!/usr/bin/python3

import fileinput

grid,antennas,answers = [],{},([0,0])

for line in open(0).readlines():
    grid.append(list(line.strip()))

for y in range(len(grid)):
    for x in range(len(grid[y])):
        c = grid[y][x];
        if c.isalnum():
            if not c in antennas:
                antennas[c] = []
            antennas[c].append([x,y])

for a in antennas:
    signals = antennas[a]
    for position in range(len(signals)):
        (thisX,thisY) = signals[position]
        for newposition in set(range(len(signals))) - {position}:
            (newX,newY) = signals[newposition]
            diffX = newX - thisX
            diffY = newY - thisY
            antiX = newX + diffX
            antiY = newY + diffY

            while 0 <= antiY <= y and 0 <= antiX <= x:
                grid[antiY][antiX] = '#'
                antiY += diffY
                antiX += diffX

for row in range(len(grid)):
    answers[0] += grid[row].count('#')
    answers[1] += len([i for i in grid[row] if i != '.'])

print(answers)
