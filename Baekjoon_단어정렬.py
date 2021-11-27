#1181번

import sys

T=int(sys.stdin.readline())
N=set()
for _ in range(T):
    N.add(sys.stdin.readline())
N=sorted(N,key=lambda x: (len(x), x))
for i in range(len(N)):
    print(N[i],end='')