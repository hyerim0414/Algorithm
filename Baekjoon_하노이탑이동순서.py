#11729번

import sys
import math

N=int(sys.stdin.readline())

def hanoi(n,a,b):
    if(n==1):
        print(a,b)
    else:
        hanoi(n-1,a,6//(a*b))
        print(a,b)
        hanoi(n-1,6//(a*b),b)


print(int(math.pow(2,N)-1))
hanoi(N,1,3)
