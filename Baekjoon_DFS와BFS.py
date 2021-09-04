#1260번

from collections import deque

def dfs(start):
    stack=[start]
    while(stack):
        cur=stack.pop()
        if(visited[cur]==0):
            visited[cur]=1
            print(cur, end=' ')
            for i in sorted(node[cur],reverse=True):
                stack.append(i)

def bfs(start):
    queue=deque([start])
    while(queue):
        cur=queue.popleft()
        if(visited[cur]==1):
            visited[cur]=0
            print(cur, end=' ')
            for i in node[cur]:
                queue.append(i)

N,E,S=map(int,input().split(" "))
node=[set() for i in range(N+1)]

for _ in range(E):
    u, v=map(int,input().split(" "))
    node[u].add(v)
    node[v].add(u)
visited=[0 for i in range(N+1)]
dfs(S)
print()
visited=[1 for i in range(N+1)]
bfs(S)
print()