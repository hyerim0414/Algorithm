
import sys

from itertools import combinations

N, M =list(map(int,sys.stdin.readline().strip().split()))

house=[]
chicken=[]

for i in range(N):
    row=list(map(int,sys.stdin.readline().strip().split()))
    for j in range(N):
        if(row[j]==1):
            house.append((i,j))
        elif(row[j]==2):
            chicken.append((i,j))

min_dist=2*N*len(house) # 최악의 상황 설정
combi=combinations(chicken,M)

#조합
for chicken_combi in combi: 
    #집마다
    tmp_dist=0
    for h in house:
        min_home_dist=2*N
        #치킨집 중 가장 가까운거 선택
        for c in chicken_combi:
            tmp=abs(h[0]-c[0])+abs(h[1]-c[1])
            min_home_dist=min(min_home_dist,tmp)
        tmp_dist+=min_home_dist
    min_dist=min(min_dist,tmp_dist)

print(min_dist)