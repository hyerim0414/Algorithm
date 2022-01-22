#1260번-220122
'''
- 간선이 이어지지 않은 경우 고려
- 런타임 에러 -> 시작점에 간선이 연결되지 않은 경우 시작점만 출력
- 기본 이론부터 다시 복습
1000 1 1
999 1000
'''

import sys
from collections import deque

N, M, start= map(int,sys.stdin.readline().split())

node=[set() for _ in range(N+1)] #정점 번호가 작은 것부터 이동

for _ in range(M):
    u,v=map(int,sys.stdin.readline().split())
    node[u].add(v)
    node[v].add(u)

def dfs(N,start):
    q=deque([start])
    while(q):
        cur=q.pop()
        if(visited[cur]==0):
            visited[cur]=1
            res.append(cur)
            if(node[cur]!=[]):
                for i in sorted(node[cur],reverse=True):
                    q.append(i) 
    return

def bfs(N,start):
    q=deque([start])
    while(q):
        cur=q.popleft()
        if(visited[cur]==0):
            visited[cur]=1
            res.append(cur)
            if(node[cur]==[]):
                break
            for i in sorted(node[cur]):
                q.append(i)
    return

visited=[0]*(N+1)
visited[0]=1
res=[]
dfs(N,start)
print(*res)
visited=[0]*(N+1)
visited[0]=1
res=[]
bfs(N,start)
print(*res)