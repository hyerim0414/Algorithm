#2178번

'''
- bfs 문제
- 이미 간 곳은 1 -> -1 로 변경
- '0001' 문자열도 list(map(int,input))을 이용해서 숫자로 변경가능 line#20
'''

import sys
from collections import deque

move=[[0,1],[0,-1],[-1,0],[1,0]] #상하좌우
Q=deque()

N, M=map(int,sys.stdin.readline().split())
Mirro=[]
min_len=N*M #최소 칸 수 구하기

for _ in range(N):
    Mirro.append(list(map(int, sys.stdin.readline()[:-1])))
    print(Mirro)


Q.append([0,0])
while(Q):
    cur_x,cur_y=Q.popleft()
    for x,y in move:
        x,y=cur_x+x,cur_y+y
        if(x<0 or y<0 or x>=N or y>=M):
            continue
        if(Mirro[x][y]==1):
            Mirro[x][y]=Mirro[cur_x][cur_y]+1
            Q.append([x,y])
        
print(Mirro[-1][-1])