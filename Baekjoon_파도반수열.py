#9461번

import sys

P=[0,1,1,1,2,2]

T=int(sys.stdin.readline())

for _ in range(T):
    N=int(sys.stdin.readline())
    if(len(P)-1 <N):
        for i in range(len(P),N+1):
            P.append(P[i-1]+P[i-5])
    print(P[N])