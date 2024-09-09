#240228
#큐
#큐2도 성공

import sys
from collections import deque

N=int(sys.stdin.readline())
queue=deque()

empty_check=['pop','front','back']

for _ in range(N):
    s=sys.stdin.readline().split()

    if(s[0]=='push'):
        queue.append(s[1])
    elif(s[0]=='size'):
        print(len(queue))
    elif(s[0]=='empty'):
        tmp=1 if(len(queue)==0) else 0
        print(tmp)
    elif((s[0] in empty_check) & (len(queue)==0)):
        print(-1)

    elif(s[0]=='pop'):
        print(queue.popleft())
    
    elif(s[0]=='front'):
        print(queue[0])
    elif(s[0]=='back'):
        print(queue[-1])

