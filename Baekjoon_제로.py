#10773번

import sys
stack=[]

K=int(sys.stdin.readline())
for _ in range(K):
    command=int(sys.stdin.readline())
    if(command==0):
        stack.pop()
    else:
        stack.append(command)
print(sum(stack))
print()