#1966번

import sys
from collections import deque

T=int(sys.stdin.readline())
for _ in range(T):
    N,M=map(int,sys.stdin.readline().split())
    important=deque(list(map(int,sys.stdin.readline().split())))
    idx=deque(range(N))
    order=1
    
    while(True):
        if(important[0]==max(important)):
            if(idx[0]==M):
                print(order)
                break
            else:
                important.popleft()
                idx.popleft()
                order+=1
        else:
            important.append(important.popleft())
            idx.append(idx.popleft())