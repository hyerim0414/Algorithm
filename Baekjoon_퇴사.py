# 240909

import sys

N = int(sys.stdin.readline())
T = []
P = []
cur =0
price = 0 

table = [list(map(int,sys.stdin.readline().split(" "))) for _ in range(N)]
res = [0 for i in range(N+1)] # 맨 마지막 1일 걸리는 스케줄에 대해 가능하기 떄문

for i in range(N-1,-1,-1):
    Ti, Pi = table[i]
    if(i+Ti > N):
        res[i]=res[i+1]
    else:
        res[i] = max(res[i+1],Pi+res[i+Ti])
    
print(max(res))