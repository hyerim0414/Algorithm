#2644번

'''
- visited에 몇번째 방문인지 적어두기
- answer까지 횟수 말고. 정답까지 간 거리를 계산해야됨
'''

import sys
from collections import deque

N=int(sys.stdin.readline())
what=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())

relation=[set() for _ in range(N+1)]
for _ in range(M):
    u,v=map(int,sys.stdin.readline().split())
    relation[u].add(v)
    relation[v].add(u)

visited=[-1]*(N+1)
visited[what[0]]+=1

def dfs(start,end):
    q=deque([start])

    while(q):
        cur=q.pop()
        for i in relation[cur]:
            if(visited[i]==-1):
                visited[i]=visited[cur]+1
                q.append(i)


dfs(what[0],what[1])
print(visited[what[1]])