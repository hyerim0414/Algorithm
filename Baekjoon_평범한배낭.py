#12865번
'''
- N : 물품 수 | K : 최대 무게
- knap[i][j]: i까지의 물품을 담으면서 최대 j 무게에서 가능한 최대 가치

'''
import sys

N,K = map(int,sys.stdin.readline().split()) 

bag = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

knap = [[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(N): 
    for j in range(1,K+1):
        if bag[i][0] <= j: #j무게 가방에 넣을 수 있으면
            knap[i+1][j] = max(knap[i][j], knap[i][j-bag[i][0]] + bag[i][1]) #넣었을 때 이득인지 비교
        else:
            knap[i+1][j]=knap[i][j]
            
print(knap[-1][-1])