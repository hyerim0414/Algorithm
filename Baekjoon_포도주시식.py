#2156번
'''
- 2579번 계단오르기 문제와는 다르게 두번 연속 안 먹는 경우가 존재
- 내 잔을 마시지 않는 경우가 더 좋을 수도 있음
'''
import sys

T=int(sys.stdin.readline())

wine=[]
for _ in range(T):
    wine.append(int(sys.stdin.readline()))
dp=[wine[0]]

if(T>1):
    dp.append(wine[0]+wine[1])
if(T>2):
    dp.append(max(wine[0]+wine[2],wine[1]+wine[2],dp[1]))
    for i in range(3,T):
        dp.append(max(dp[i-3]+wine[i-1]+wine[i],dp[i-2]+wine[i],dp[i-1]))  
print(dp[-1])