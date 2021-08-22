#2565번

import sys

T=int(sys.stdin.readline())
line=[]
dp=[0 for _ in range(T)]
for _ in range(T):
    line.append(list(map(int,sys.stdin.readline().split())))

line=sorted(line,key= lambda x: x[0])

for i in range(T):
    for j in range(i):
        if(line[i][1]>line[j][1] and dp[i]<dp[j]):
            dp[i]=dp[j]
    dp[i]+=1 #자기 자신

print(T-max(dp))
