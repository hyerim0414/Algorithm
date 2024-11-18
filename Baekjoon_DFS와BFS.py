'''
241118
- 방문가능한 정점 여러개 => 번호가 작은 것부터 방문
- 방문할 점 없는 경우 종료

* 배운점
- list앞에 *을 붙이고 print하면 [] 없이 리스트 원소 출력가능
- set 은 순서가 없으므로, 작은 번호부터 방문이라는 규칙을 위해서는 sorted()함수 적용해야함
'''

import sys
from collections import deque

N, M, start_node = list(map(int,sys.stdin.readline().split()))

graph = [set([]) for _ in range(N+1)] # linked list로 

for _ in range(M):
    i,j = list(map(int,sys.stdin.readline().split()))
    graph[i].add(j)
    graph[j].add(i)

global dfs_res
dfs_res = []
def dfs(graph, start_node, visited = [False for _ in range(N+1)]):
    visited[start_node]= True
    dfs_res.append(start_node)
    for i in graph[start_node]:
        if not visited[i]:
            dfs(graph,i,visited)
    return dfs_res

def dfs_2(graph, start_node, visited = [False for _ in range(N+1)]):
    res = []
    queue = deque([start_node])
    while queue:
        cur = queue.pop()
        if not visited[cur]:
            visited[cur] = True
            res.append(cur)
            for i in sorted(graph[cur],reverse=True):
                queue.append(i)
    return res

def bfs(graph, start_node, visited = [False for _ in range(N+1)]):
    res = []
    queue = deque([start_node])
    while queue:
        cur = queue.popleft()
        if not visited[cur]:
            visited[cur]=True
            res.append(cur)
            for i in sorted(graph[cur]):
                queue.append(i)
    return res

    

print(*dfs_2(graph, start_node))
print(*bfs(graph, start_node))