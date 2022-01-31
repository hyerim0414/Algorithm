#2568번

import sys

T=int(sys.stdin.readline())
line=[]
dp=[[0,0] for i in range(T)]
for _ in range(T):
    line.append(list(map(int,sys.stdin.readline().split())))

line=sorted(line,key=lambda x: x[0])

#선형탐색 - O(n^2)으로 시간초과
for i in range(T):
    for j in range(i):
        if(line[j][1]<line[i][1] and dp[i][1]<dp[j][1]):
            dp[i][1]=dp[j][1]
    dp[i][0]=line[i][0]
    dp[i][1]+=1

temp=dp[-1][1]
a=set([dp[i][0] for i in range(T)])
b=set([dp[-1][0]])
for i in range(T-1,-1,-1):
    if(temp>dp[i][1]):
        b.add(dp[i][0])
        temp=dp[i][1]
print(len(a-b))
for i in a-b:
    print(i)

        