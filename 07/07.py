#!/usr/bin/python3

import fileinput

parts=[0,0]

def to_base(number, base):
    digits = []
    while number:
        digits.append(number % base)
        number //= base
    return list(reversed(digits))

for line in open(0).readlines():
    a=line.split()
    testvalue = int(a[0].strip(':'))
    del a[0]
    x=len(a)-1

    for base in [ 2, 3 ]:
        combinations = base ** x
        for c in range(combinations):
            zz = to_base(c,base)
            zz = [0] * (x-len(zz)) + zz
            result = 0
            val1 = int(a[0])
            for d in range(x):
                val2=int(a[d+1])
                if zz[d] == 0:
                    result = val1 + val2
                elif zz[d] == 1:
                    result = val1 * val2
                else:
                    result = int(str(val1) + str(val2))
                val1 = result 
            if result == testvalue:
                parts[base-2] += result
                break

print(parts)
