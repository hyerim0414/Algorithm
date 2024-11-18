'''
241118
- 배추흰지렁이 -> 인접한 배추로 이동 & 해충으로부터 보호 가능
- 상하좌우로 움직일 수 있음
- 배추 1, 땅 0
- 그래프 탐색으로 갈 수 있는 곳은 하나의 집합 = 지렁이 최소 1개 필요
- 상하좌우 움직일 때 board 벗어나는지 체크해야함

'''
import sys
from collections import deque
dmove = [(1,0),(0,1),(-1,0),(0,-1)]
# 테스트 케이스 개수 T
T = int(sys.stdin.readline())
res= []
for _ in range(T):
    # 가로 M, 세로 N, 배추 개수 K
    M, N, K = list(map(int,sys.stdin.readline().split()))

    # 배추 위치만 중요한듯 -> graph 전체를 표현할 필요 없음
    # list로 하면 방문했는지 체크할때마다 O(n) -> 2차원 배열로 T/F라벨링
    visited = [[True for _ in range(N)] for _ in range(M)]
    graph = deque([])
    
    # 배추 위치 x,y
    for _ in range(K):
        x,y = list(map(int,sys.stdin.readline().split()))
        graph.append([x,y])
        visited[x][y]=False # 땅=T, 배추=F에서 시작

    tmp = 0
    # 새롭게 탐색 시작
    for cur in graph:
        if not visited[cur[0]][cur[1]]:
            tmp+=1
            queue = deque([cur])
            while queue:
                cx,cy = queue.popleft()
                if not visited[cx][cy]:
                    visited[cx][cy]=True
                    for dx,dy in dmove:
                        nx,ny = cx+dx,cy+dy
                        if((0<= nx < M ) and (0<= ny<N)):
                            queue.append([nx,ny])

    res.append(tmp)
                            
print(*res,sep="\n")

