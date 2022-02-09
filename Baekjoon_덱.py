#10866번

from collections import deque
import sys

q=deque([])
n=int(sys.stdin.readline())
for _ in range(n):
    s=list(sys.stdin.readline().split())

    if(s[0]=='push_front'):
        q.appendleft(int(s[1]))
    elif(s[0]=='push_back'):
        q.append(int(s[1]))
    elif(s[0]=='pop_front'):
        if(q):
            print(q.popleft())
        else:
            print(-1)
    elif(s[0]=='pop_back'):
        if(q):
            print(q.pop())
        else:
            print(-1)
    elif(s[0]=='size'):
        print(len(q))
    elif(s[0]=='empty'):
        print(0) if(q) else print(1)
    elif(s[0]=='front'):
        print(q[0]) if(q) else print(-1)
    elif(s[0]=='back'):
        print(q[-1]) if(q) else print(-1)