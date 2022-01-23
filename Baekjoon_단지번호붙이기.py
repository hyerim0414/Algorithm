#2667번

import sys
from collections import deque

N=int(sys.stdin.readline())
node=[]
res=[]

for _ in range(N):
    node.append(list(map(int, sys.stdin.readline()[:-1])))

move=[[1,0],[0,-1],[-1,0],[0,1]]

def bfs(x,y):
    q=deque([[x,y]])
    temp=0
    while(q):
        cur_x,cur_y=q.popleft()
        if(node[cur_x][cur_y]==1):
            node[cur_x][cur_y]=0
            temp+=1
            for mx,my in move:
                if((cur_x+mx)<0 or (cur_x+mx)>=N or (cur_y+my)<0 or (cur_y+my)>=N ):
                    continue
                q.append([cur_x+mx,cur_y+my])
    res.append(temp)

for i in range(0,N):
    for j in range(0,N):
        if(node[i][j]==1):
            bfs(i,j)

print(len(res))
for i in sorted(res):
    print(i)

