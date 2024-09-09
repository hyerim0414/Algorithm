#24.02.29
#큐

import sys
from collections import deque

N=int(sys.stdin.readline())
queue=deque(range(1,N+1))
res=[]

while(len(queue)>1):
    res.append(queue.popleft())
    queue.append(queue.popleft())
res.append(queue.popleft())

print(' '.join(list(map(str,res))))