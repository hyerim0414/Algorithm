#1676번

import sys
from math import factorial

n=int(sys.stdin.readline())

N=str(factorial(n))
ct=0
i=1
while(True):
    if(N[-i]!='0'):
        break
    else:
        ct+=1
        i+=1

print(ct)