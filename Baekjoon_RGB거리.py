#1149번

import sys

T=int(sys.stdin.readline())
color_cost=[]

for _ in range(T):
    color_cost.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,T):
    for j in range(3):
        color_cost[i][j]+=min(color_cost[i-1][:j]+color_cost[i-1][j+1:])
print(min(color_cost[-1]))