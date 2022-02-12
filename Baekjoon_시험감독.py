#13458번

import readline
import sys
import math

N=int(sys.stdin.readline())
cs=list(map(int,sys.stdin.readline().split()))
B,C=map(int,sys.stdin.readline().split())

ans=N

for i in cs:
    if(i-B<=0):
        continue
    ans+=math.ceil((i-B)/C)

print(ans)