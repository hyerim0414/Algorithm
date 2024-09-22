# 240921

'''
고려해야하는 사항
- dmove에 대한 for문을 돌 때, 정답과 오답 둘 다 존재한다면 정답 O

'''
import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split(" "))
# strip() 문자열 공백 제거 
board = [ list(sys.stdin.readline().strip()) for _ in range(N)]
visited = []

for i in range(1,N-1):
    for j in range(1,M-1):
        if(board[i][j]=='R'):
            red = [i,j]
            board[i][j]='.'
        elif(board[i][j]=='B'):
            blue = [i,j]
            board[i][j] = '.'

q = deque([red+blue+[0]])
dmove = [[0,1],[1,0],[-1,0],[0,-1]]
def bfs(position, move):
    red = position[0:2]
    blue = position[2:4]
    cnt = position[-1]
    
    cnt_r = 0
    cnt_b = 0
    while(board[red[0]+move[0]][red[1]+move[1]]=='.'):
        red[0]+=move[0]
        red[1]+=move[1]
        cnt_r+=1

    while(board[blue[0]+move[0]][blue[1]+move[1]]=='.'):
        blue[0]+=move[0]
        blue[1]+=move[1]
        cnt_b+=1 
    
    if(board[red[0]+move[0]][red[1]+move[1]] == 'O'):
        if(red!= blue):
            return cnt+1
        else:
            return 0
    elif(board[blue[0]+move[0]][blue[1]+move[1]] == 'O'):
        return 0
    elif(red == blue):
        if(cnt_r < cnt_b):
            blue[0]-=move[0]
            blue[1]-=move[1]
        else:
            red[0]-=move[0]
            red[1]-=move[1]     
    if(red+blue not in visited):
        q.append(red+blue+[cnt+1])
        visited.append(red+blue)

    return 0

def find_hall():
    while q:
        cur = q.popleft()
        if(cur[-1]==10):
            return -1
        else:
            for d in dmove:
                res=bfs(cur,d)
                if(res >0 ):
                    return res
    return -1

print(find_hall())
    
