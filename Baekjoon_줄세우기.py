#2252번

'''
- 위상정렬 
'''

import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split())

graph=[[] for _ in range(N+1)]
student=[0]*(N+1)  #진입 차수

for _ in range(M):
    a,b=map(int,sys.stdin.readline().split()) #a<b = a -> b
    student[b]+=1
    graph[a].append(b)

q=deque()
result=[]

for i in range(1,N+1):
    if(student[i]==0):
        q.append(i)

while  q:
    cur=q.popleft()
    result.append(cur)
    for i in graph[cur]:
        student[i]-=1
        if(student[i]==0):
            q.append(i)

print(*result)


