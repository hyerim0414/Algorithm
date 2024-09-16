# 240916

import sys
from collections import deque

N, X = map(int, sys.stdin.readline().split())

visitor = list(map(int, sys.stdin.readline().split()))

res = [0 for _ in range(N-X+1)]

q1 = deque(visitor[:X])
q2 = deque(visitor[X:])

res = sum(visitor[0:X])
max_val = res
cnt = 1
while q2:
    cur_r = q2.popleft()
    cur_l = q1.popleft()
    q1.append(cur_r)
    res += cur_r -cur_l
    if(max_val<res):
        max_val = res
        cnt=1
    elif(max_val == res):
        cnt+=1
    


if(max_val==0):
    print("SAD") 
else:
    print(max_val)
    print(cnt) 