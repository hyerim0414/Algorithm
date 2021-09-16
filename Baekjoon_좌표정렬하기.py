#11650번

import sys

T=int(sys.stdin.readline())
N=[ list(map(int,sys.stdin.readline().split())) for _ in range(T)]
N=sorted(N,key=lambda x: (x[0],x[1]))

for i in range(T):
    print(*N[i])