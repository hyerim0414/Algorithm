#24.23.09
#큐

import sys
from collections import deque

N=int(sys.stdin.readline())

queue=deque()

while(1):
    x=int(sys.stdin.readline())
    if (x==-1):
        break
    elif(x==0):
        queue.popleft()
    else:
        if(len(queue)<N):
            queue.append(x)

if(len(queue)==0):
    print("empty")
else:
    print(' '.join(map(str,queue)))


