# 하는중

import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split(" "))
# strip() 문자열 공백 제거 
board = [ list(sys.stdin.readline().strip()) for _ in range(N)]

res = -1
# O(100)
for i in range(1,N-1):
    for j in range(1,M-1):
        if(board[i][j]=='R'):
            red = [i,j]
        elif(board[i][j]=='B'):
            blue = [i,j]
dmove = [[0,1],[1,0],[-1,0],[0,-1]]
queue_r = deque([red])
queue_b = deque([blue])

for i in range(10):
    
    cur_r = queue_r.popleft()
    cur_b = queue_b.popleft()
    #print(cur_r)
    for dx,dy in dmove:

        tmp_r = cur_r
        tmp_b = cur_b 
        while(board[tmp_r[0]+dx][tmp_r[1]+dy] == '.'):
            tmp_r[0]+=dx
            tmp_r[1]+=dy
        while(board[tmp_b[0]+dx][tmp_b[1]+dy] == '.'):
            tmp_b[0]+=dx
            tmp_b[1]+=dy
        print(tmp_r+[dx,dy])
        if(board[tmp_r[0]+dx][tmp_r[1]+dy] == 'O' 
           and board[tmp_b[0]+dx][tmp_b[1]+dy] != 'O'):
            res  = i+1
        else:
            queue_r.append(tmp_r)
            queue_b.append(tmp_b)
    if(res!=-1):
        break
print(res)