# 240228
# 240926
#큐
#요세푸스 문제와 유사



import sys
from collections import deque

N = int(sys.stdin.readline().strip())
q = deque([i for i in range(1,N+1)])

while(len(q)>2):
    q.popleft()
    q.append(q.popleft())

print(q[-1])
