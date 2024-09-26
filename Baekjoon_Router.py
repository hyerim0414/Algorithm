#24.23.09
# 240926
#큐

import sys
from collections import deque

N = int(sys.stdin.readline().strip())
q = deque([])
ck = 0

while True:
    cur = int(sys.stdin.readline().strip())
    if(cur == -1):
        break
    if(cur >0 and ck<N):
        q.append(cur)
        ck+=1
    elif(cur == 0):
        q.popleft()
        ck-=1

if(ck>0):
    print(" ".join(map(str,q)))
else:
    print("empty")