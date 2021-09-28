#11049번

'''
- A*(B*C) , (A*B)*C 
'''

import sys
import math

T=int(sys.stdin.readline())

mat=[list(map(int,sys.stdin.readline().split())) for _ in range(T)]
DP=[[0 for _ in range(T)] for _ in range(T)]
for i in range(T-1):
    DP[i][i+1]=mat[i][0]*mat[i][1]*mat[i+1][1] 

for i in range(1,T): 
    for start in range(T):
        end=start+i
        if(end>=T or start>=T):
            break
        DP[start][end]=math.pow(2,31)
        for k in range(start,end): 
            DP[start][end]=min(DP[start][end], DP[start][k]+DP[k+1][end]+mat[start][0]*mat[k][1]*mat[end][1])
print(DP[0][T-1])
    
    