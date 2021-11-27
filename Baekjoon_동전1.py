#2293번
import sys

n,k=map(int,sys.stdin.readline().split())
coin=[int(sys.stdin.readline()) for _ in range(n)]

DP=[0 for _ in range(k+1)]
DP[0]=1 #한가지 종류의 코인을 이용해서 만드는 방법
for c in coin:
    for i in range(c,k+1):
        if(i-c>=0):
            DP[i]+=DP[i-c]

print(DP[k])

