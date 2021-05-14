"""
- shortest path search algorithm 중 Dijkstra's algorithm 이용
- bfs 인접 노드 탐색, minheap 이용
- 제한사항 : 두 마을을 연결하는 도로는 여러개 있을 수 있다. 따라서, 이중 딕셔너리 사용하지 않음

"""

import heapq
def GraphPath(N,road,K):
    count=0
    INF=500000
    #그래프 생성
    G={}
    minheap=[[1,0]]
    distance=[INF]*(N+1)
    distance[1]=0
    for i in range(1,N+1):
        G[i]=[] 
    for r in road:
        v1, v2= r[0], r[1]
        G[v1].append([v2,r[2]])
        G[v2].append([v1,r[2]])

    while(minheap!=[]):
        node=heapq.heappop(minheap)
        for adjacent, cost in G[node[0]]:
            #인접 노드의 cost가 update되면 push
            if((node[1]+cost)<distance[adjacent]):
                distance[adjacent]=node[1]+cost
                heapq.heappush(minheap,[adjacent,distance[adjacent]])

    for i in range(len(distance)):
        if(distance[i]<=K): count+=1
        
    return count

