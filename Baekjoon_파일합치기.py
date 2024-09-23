# 240923

# dp[i][j] : i~j 까지를 합쳤을 때 가장 작은 합 (누적합)
# 50 30 30 40 => (50+30) + (30+40) + (80)+(70) 
# 이런식으로 기존 파일 크기가 누적합으로 계속 들어감

import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    K = int(sys.stdin.readline().strip())
    F = list(map(int,sys.stdin.readline().split()))
    dp = [[100000000 for _ in range(K)] for _ in range(K)]
    tmp =  [sum(F[0:i]) for i in range(1,K+1)]
    for i in range(K):
        dp[i][i] = 0 # 누적합 뒤에서 하니까 여기선 0으로 넣어주기
    
    for line in range(1,K):

        for i in range(K-line):
            j = i + line
            for k in range(i,j):
                dp[i][j] = min(dp[i][k]+dp[k+1][j]+ tmp[j]-tmp[i]+F[i],dp[i][j]) 
    print(dp[0][K-1])

