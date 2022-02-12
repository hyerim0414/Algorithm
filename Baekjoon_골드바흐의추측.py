#6588번

import sys

oddP=[False,False]+[True]*1000000

def prime_make():
    for i in range(2,1001):
        if(oddP[i]==True):
            for j in range(i+i,1000001,i):
                oddP[j]=False
    return

prime_make()

while(True):
    n=int(sys.stdin.readline())
    if(n==0):
        break
    for i in range(3,1000000,2):
        if(oddP[i]==True and oddP[n-i]==True):
            print("{} = {} + {}".format(n,i,n-i))
            break
    