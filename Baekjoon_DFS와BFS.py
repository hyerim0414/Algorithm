#1260번-220121

import sys
from collections import deque

N, M, start= map(int,sys.stdin.readline().split())

node=[set() for _ in range(N+1)] #정점 번호가 작은 것부터 이동

for _ in range(M):
    u,v=map(int,sys.stdin.readline().split())
    node[u].add(v)
    node[v].add(u)

def dfs(N,start):
    res=[]
    visited=[0]*(N+1)
    visited[0]=1
    q=deque([start])
    while(q):
        cur=q.pop()
        if(visited[cur]==0):
            visited[cur]=1
            res.append(cur)
            for i in sorted(node[cur],reverse=True):
                q.append(i)
    print(*res)
    return

def bfs(N,start):
    res=[]
    visited=[0]*(N+1)
    visited[0]=1
    q=deque([start])
    while(q):
        cur=q.popleft()
        if(visited[cur]==0):
            visited[cur]=1
            res.append(cur)
            for i in node[cur]:
                q.append(i)
    print(*res)


dfs(N,start)
bfs(N,start)