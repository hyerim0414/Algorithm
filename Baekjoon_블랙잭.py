#2798번
'''
- 브루트 포스
'''
import sys 

N,M=map(int,sys.stdin.readline().split())
card=list(map(int,sys.stdin.readline().split()))

max_sum=0

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if(card[i]+card[j]+card[k]<=M):
                max_sum=max(card[i]+card[j]+card[k],max_sum)

print(max_sum)