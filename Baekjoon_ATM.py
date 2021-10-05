#11399번
'''
- 정렬 후 누적합
'''

import sys

N=int(sys.stdin.readline())
people=list(map(int,sys.stdin.readline().split()))
people=sorted(people)
ans=people[0]
temp=people[0]
for i in range(1,N):
    temp+=people[i]
    ans+=temp

print(ans)