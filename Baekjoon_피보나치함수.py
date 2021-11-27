#1003번 

import sys

count=[[1,0],[0,1],[1,1]]
T=int(sys.stdin.readline())


for _ in range(T):
    N=int(sys.stdin.readline())
    if(len(count)<=N):
        for i in range(len(count),N+1):
            z=count[i-1][0]+count[i-2][0]
            o=count[i-1][1]+count[i-2][1]
            count.append([z,o])
    print(*count[N])
