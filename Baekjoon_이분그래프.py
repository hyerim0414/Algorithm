#1707번

import sys
from collections import deque

def bfs(node,start):
    q=deque([start])
    while(q):
        cur=q.popleft()
        color=visited[cur]
        for i in node[cur]:
            if(visited[i]==0):
                visited[i]=color*(-1)
                q.append(i)
            elif(visited[i]==color):
                return False
    return True

K=int(sys.stdin.readline())
for _ in range(K):
    V,E=map(int,sys.stdin.readline().split())
    node=[set()for _ in range(V+1)]

    for _ in range(E):
        u,v=map(int,sys.stdin.readline().split())
        node[u].add(v)
        node[v].add(u)
    
    visited=[0]*(V+1) 
    flag=0

    for i in range(1,V+1):
        if(visited[i]==0):
            visited[i]=1
            if not bfs(node,i):
                flag=-1
                break
    if (flag==0):
        print("YES")  
    else:
        print("NO")
