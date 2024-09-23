# 240923
# bottom-up

import sys

N = int(sys.stdin.readline().strip())

dp = [0] *1001

dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 1

for i in range(4,N+1):
    dp[i] = min(dp[i-1],dp[i-3])+1

if(dp[N] % 2==0):
    print("CY")
else:
    print("SK")

