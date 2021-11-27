#2579번
'''
- 배열을 입력받을 시 append 함수 사용하는 것이 효율적
'''
import sys

T=int(sys.stdin.readline())
score=[]
for _ in range(T):
    score.append(int(sys.stdin.readline()))
dp=[score[0]]
if(T>1):
    dp.append(score[0]+score[1])
if(T>2):
    dp.append(max(score[0]+score[2],score[1]+score[2]))
    for i in range(3,T):
        dp.append(max(dp[i-3]+score[i-1]+score[i],dp[i-2]+score[i]))

print(dp[-1])
