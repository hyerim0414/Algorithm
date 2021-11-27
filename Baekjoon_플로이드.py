#11404번
'''
- 플로이드-와샬 알고리즘 : k 노드를 거쳐가는 정점 고려하여 최단 거리 계산
- dynamic programming
- maxsize를 import 하지 않고 100000정도로 설정하면 너무 작아서 틀림
'''
import sys
from sys import maxsize

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
city=[[maxsize]*(n+1) for _ in range(n+1) ]
for i in range(n+1):
    city[i][i]=0

for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    city[a][b]=min(city[a][b],c)
       
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(k==i or k==j or i==j):
                continue
            city[i][j]=min(city[i][j],city[i][k]+city[k][j])


for i in range(1,n+1):
    for j in range(1,n+1):
        if(city[i][j]==maxsize):
            print(0,end=' ')
        else:
            print(city[i][j],end=' ')
    print()