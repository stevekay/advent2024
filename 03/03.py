#!/usr/bin/python3

import fileinput
import re

pattern = re.compile(r'(?P<mode>do\(\)|don\'t\(\)|mul\((?P<a>\d{1,3}),(?P<b>\d{1,3})\))')

partone = 0
parttwo = 0
enabled = 1

for line in fileinput.input():
    for m in re.finditer(pattern,line):
        if m.group('mode') == "do()":
            enabled = 1
        elif m.group('mode') == "don't()":
            enabled = 0
        else:
            v = int(m.group('a')) * int(m.group('b'))
            partone += v
            parttwo += v * enabled

print(partone,parttwo)
