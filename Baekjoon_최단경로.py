#1753번
''''
- 다익스트라 알고리즘 이용
- 일반 큐 사용시 O(v^2), 힙큐 사용시 O(elogv)
'''

import sys
import heapq

n,m=map(int,sys.stdin.readline().split())
inf=sys.maxsize
k=int(sys.stdin.readline())

graph=[[]*(n+1) for _ in range(n+1)]

dist=[inf]*(n+1)
heap=[]

for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append((b, c))


def dijkstra(start):
    dist[start]=0
    heapq.heappush(heap, (0, start))

    while heap:
        d, now = heapq.heappop(heap)

        if dist[now] < d: #업데이트 완료
            continue
        
        for i in graph[now]: #인접노드 확인
            cost = d + i[1] #start -> now -> 인접노드 가는 비용
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))


dijkstra(k)

for i in range(1, n+1):
    if dist[i] == inf:
        print("INF")
    else:
        print(dist[i])