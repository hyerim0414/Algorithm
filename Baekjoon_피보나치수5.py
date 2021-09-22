#10870번

import sys

N=int(sys.stdin.readline())

def fibonacci(n):
    if(n==1 or n==0):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(N))