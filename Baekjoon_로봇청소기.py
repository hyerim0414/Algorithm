#14503번
'''
- 왼쪽으로 회전하면서 search
'''
import sys

N,M=map(int,sys.stdin.readline().split())
r,c,D=map(int,sys.stdin.readline().split())
graph=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

ck=[[-1,0],[0,1],[1,0],[0,-1]] 
cur=[r,c]
clean=0

flag=0
global d
d=D
while(True):
    if(graph[cur[0]][cur[1]]==0):
        #print(*cur,d)
        clean+=1
        graph[cur[0]][cur[1]]=clean+3
    flag=-1
    for _ in range(4):
        nd=(d+3)%4
        nx,ny=ck[nd] #nd를 d로 해서 오류
        nx,ny=[cur[0]+nx,cur[1]+ny]
        d=nd
        if(graph[nx][ny]==0):
            flag=0
            cur=[nx,ny]
            break
    if(flag==-1):
        nx,ny=ck[(d+2)%4]
        nx,ny=[cur[0]+nx,cur[1]+ny]
        if(graph[nx][ny]!=1):
            cur=[nx,ny]
        else:
            break

print(clean)

'''6 6
2 1 3
1 1 1 1 1 1
1 0 0 0 0 1
1 0 1 1 1 1
1 0 1 1 1 1
1 0 1 1 1 1
1 1 1 1 1 1'''


'''
3 3
1 1 0
1 1 1
1 0 1
1 1 1
'''