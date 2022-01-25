#5014번
'''
- bfs 문제 
'''

import sys
from collections import deque

F,S,G,U,D= map(int,sys.stdin.readline().split())
visited={S}

def bfs(f,s,g,u,d):
    q=deque([[s,0]])
    while(q):
        cur,m=q.popleft()
        if(cur==g):
            return m
        if(cur+u<=f and cur+u not in visited):
            q.append([cur+u,m+1])
            visited.add(cur+u)
        if(cur-d>=1 and cur-d not in visited):
            q.append([cur-d,m+1])
            visited.add(cur-d)
    return "use the stairs"

print(bfs(F,S,G,U,D))