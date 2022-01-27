#11003번

import sys
from collections import deque

N, D=map(int,sys.stdin.readline().split())
num=list(map(int,sys.stdin.readline().split()))

d=deque()
res=[]

for id,cur in enumerate(num):
    while(d and d[-1][1]>cur):
        d.pop()
    d.append([id,cur])
    while(d and d[0][0]<(id-D+1)):
        d.popleft()
    print(d[0][1],end=" ")
print()


'''
12 3
1 5 2 3 6 2 3 7 3 5 2 6
'''
