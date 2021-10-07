#1541번
'''
- '-'마다 잘라서, 각자 합한 후 빼주기
'''

import sys

num=sys.stdin.readline()[:-1].split('-') 
N=[list(map(int,x.split('+'))) for x in num]

ans=sum(N[0])
for i in range(1,len(N)):
    ans-=sum(N[i])

print(ans)
