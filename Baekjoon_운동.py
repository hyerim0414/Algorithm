#1956번
'''
- 플로이드 와샬 알고리즘 이용
- 11404번: 플로이드랑 차이점은 i->i로 가는 경우를 출력
'''
import sys

n,m=map(int,sys.stdin.readline().split())

city=[[10001]*(n+1) for _ in range(n+1)]


count=0

for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    city[a][b]=min(city[a][b],c)


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(k==i or k==j):
                continue
            city[i][j]=min(city[i][j],city[i][k]+city[k][j])

ans=10001
for i in range(1,n+1):
    ans=min(ans,city[i][i])

print(ans) if(ans!=10001) else print(-1)
