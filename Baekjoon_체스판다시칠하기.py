#1018번

import sys 

N,M=map(int,sys.stdin.readline().split())
board=[sys.stdin.readline() for _ in range(N)]
pre=board[0][0]
change=64
case1,case2=['BW','WB']
for i in range(N-7):
    for j in range(M-7):
        temp1,temp2=0,0 #BW or WB
        for row in range(i,i+8):
            for col in range(j, j+8):
                if(case1[(row+col)%2]!=board[row][col]):
                    temp1+=1
                if(case2[(row+col)%2]!=board[row][col]):
                    temp2+=1
        change=min(change,temp1,temp2)

print(change)