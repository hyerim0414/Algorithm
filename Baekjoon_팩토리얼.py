#10872번

import sys

N=int(sys.stdin.readline())

def factorial(n):
    if(n==0):
        return 1
    if(n==1 or n==2):
        return n
    else:
        return factorial(n-1)*n

print(factorial(N))
