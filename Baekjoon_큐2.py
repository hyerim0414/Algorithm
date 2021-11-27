#18258번

import sys
from collections import deque
queue=deque()

N=int(sys.stdin.readline())
for _ in range(N):
    command=sys.stdin.readline().split()
    if(command[0]=="push"):
        queue.append(int(command[1]))
    elif(command[0]=="pop"):
        print(queue.popleft() if(queue) else -1)
    elif(command[0]=="size"):
        print(len(queue))
    elif(command[0]=="empty"):
        num=0 if(queue) else 1
        print(num)
    elif(command[0]=="front"):
        print(queue[0] if(queue) else -1)
    elif(command[0]=="back"):
        print(queue[-1] if(queue) else -1)
print()