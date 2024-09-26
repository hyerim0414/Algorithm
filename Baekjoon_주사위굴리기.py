# 240925

import sys

N, M, x, y, K = list(map(int,sys.stdin.readline().split()))

board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

move = list(map(int,sys.stdin.readline().split()))

dice = [0 for _ in range(6)]

moving_idx = {1:[3,1,0,5,4,2],2:[2,1,5,0,4,3],3:[4,0,2,3,5,1], 4:[1,5,2,3,0,4]}
direction = {1:[0,1],2:[0,-1],3:[-1,0],4:[1,0]}

for cur_d in move:
    dx,dy = direction[cur_d]
    if(0<=x+dx<N and 0<=y+dy<M):
        x += dx
        y += dy
        dice = [dice[i] for i in moving_idx[cur_d]]
        if(board[x][y] ==0):
            board[x][y] = dice[-1]
        else:
            dice[-1]=board[x][y]
            board[x][y]=0
        print(dice[0])
        


