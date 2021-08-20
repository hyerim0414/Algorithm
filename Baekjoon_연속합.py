#1912번

import sys

T=int(sys.stdin.readline())

seq=list(map(int,sys.stdin.readline().split()))
dp=[0 for _ in range(T)]
dp[0]=seq[0]

for i in range(1,T):
        dp[i]=max(seq[i]+dp[i-1],seq[i])

print(max(dp))