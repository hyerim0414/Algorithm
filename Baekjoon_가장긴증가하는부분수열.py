#11053번

import sys

T=int(sys.stdin.readline())

dp=[0 for _ in range(T)]
seq=list(map(int,sys.stdin.readline().split()))

for i in range(T):
    for j in range(i):
        if(seq[i]>seq[j] and dp[i]<dp[j]):
            dp[i]=dp[j]
    dp[i]+=1 #자기 자신

print(max(dp))