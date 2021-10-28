#1504번
'''
- 다익스트라 함수 이용
'''

import sys
import heapq

n,m=map(int,sys.stdin.readline().split())
inf=sys.maxsize

graph=[[] for _ in range(n+1)]


for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

v1,v2=map(int,sys.stdin.readline().split())

def dijkstra(start,end):
    heap=[]
    dist=[inf]*(n+1)
    dist[start]=0
    heapq.heappush(heap, (0, start))

    while heap:
        d, now = heapq.heappop(heap)

        if dist[now] < d: #업데이트 완료
            continue
        
        for w,v in graph[now]: #인접노드 확인
            if(dist[v]>dist[now]+w):
                dist[v] = dist[now]+w
                heapq.heappush(heap, (dist[v], v))
    return dist[end]

opt1=dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,n)
opt2=dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,n)


if(min(opt1,opt2)<sys.maxsize) :
    print(min(opt1,opt2)) 
else :
     print("-1")
