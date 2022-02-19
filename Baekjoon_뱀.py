#3190번

import sys
from collections import deque

dir={"L":-1,"D":1}
direction=[[0,1],[1,0],[0,-1],[-1,0]]

N=int(sys.stdin.readline())
K=int(sys.stdin.readline())
node=[[0]*N for _ in range(N)]
q=deque([0,0])
mid=0
cur_x,cur_y=[0,1]

for _ in range(K):
    x,y=map(int,sys.stdin.readline().split())
    node[x-1][y-1]=1

C=int(sys.stdin.readline())
time=deque()
ct=0

for _ in range(C):
    x,c=sys.stdin.readline().split()
    time.append([int(x),dir[c]])

while(True):
    ct+=1
    if( cur_x<0 or cur_x>=N  or cur_y>=N or cur_y<0):
        break
    if(node[cur_x][cur_y]==0):
        q.popleft()
    else:
        node[cur_x][cur_y]=0
         
    if([cur_x,cur_y] in q):
        break
    q.append([cur_x,cur_y])

    if(time and ct==time[0][0]):
        x,c=time.popleft()
        mid=(mid+c)%4
    cur_x+=direction[mid][0]
    cur_y+=direction[mid][1]

print(ct)


    

