#!/usr/bin/python3

import fileinput

partone=0

for line in open(0).readlines():
    a=line.split()
    testvalue = int(a[0].strip(':'))
#    print("line=",a)
    del a[0]
    combinations = 2 ** (len(a)-1)
    ok=0
    for c in range(0,combinations):
#        print("combo",c)
        out = str(testvalue)+" -> "
        l = len(a)-1
        z = f'{c:0{l}b}'
        cur = int(a[0])
        out=str(a[0])
        result=0
        for d in range(0,len(a)-1):
            if d == 0:
                val1=int(a[d])
            else:
                val1=result
            if d > -1 :
                val2=int(a[d+1])
                if z[d] == '0':
                    result = val1 + val2
                    out = out + " + " + str(val2)
                    oper = '+'
                if z[d] == '1':
                    out = out + " * " + str(val2)
                    result = val1 * val2
                    oper = '*'
        #        print(out)
        #        print(" d=",d,"-> val1=",val1," val2=",val2,"oper=",oper,"result=",result)
#        print("result=",result)
        if result == testvalue:
            ok=1
    if ok == 1:
        partone += testvalue
#    print(" ")
#    print(" ")

print(partone)
