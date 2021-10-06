#13305번
'''
- 그순간의 최소 가격
'''
import sys

N=int(sys.stdin.readline())
distance=list(map(int,sys.stdin.readline().split()))
cost=list(map(int,sys.stdin.readline().split()))[:-1]
cur_min=cost[0]
cur_dist=distance[0]
ans=0
for i in range(1,N-1):
    if(cost[i]<cur_min):
        ans+=(cur_dist*cur_min)
        cur_dist,cur_min=distance[i],cost[i]
    else:
        cur_dist+=distance[i]
ans+=(cur_dist*cur_min)

print(ans)
