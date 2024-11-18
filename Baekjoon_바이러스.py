# 241118
# 2606번

import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
global visited
visited = [False for _ in range(N+1)]

for i in range(M):
    i, j = list(map(int,sys.stdin.readline().split()))
    graph[i].append(j)
    graph[j].append(i)

# start node = 1
# 1번에서 시작하는 그래프 탐색 (bfs/dfs)

def bfs(graph, v):
    visited[v] = True
    queue = deque([v])
    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

def dfs(graph, v):
    visited[v] = True
    queue = deque([v])
    while queue:
        cur = queue.pop()
        for i in graph[cur]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

# bfs(graph, 1)
dfs(graph,1)
print(sum(visited)-1)