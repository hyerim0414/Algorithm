#2606번

import sys
from collections import deque

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())

node=[set() for _ in range(N+1)]

for _ in range(M):
    u,v=map(int,sys.stdin.readline().split())
    node[u].add(v)
    node[v].add(u)

def bfs(N,start):
    visited=[0]*(N+1)
    res=-1
    q=deque([start])
    while(q):
        cur=q.popleft()
        if(visited[cur]==0):
            visited[cur]=1
            res+=1
            for i in node[cur]:
                q.append(i)
    print(res)


bfs(N,1)