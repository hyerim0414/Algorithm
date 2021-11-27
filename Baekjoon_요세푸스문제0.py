#11866번
'''
- K-1만큼 뒤로 옮긴 후, 맨 앞에 있는 수 제거 반복
'''

import sys
from collections import deque

N,K=map(int,sys.stdin.readline().split())
queue=deque(range(1,N+1))
answer='<'
while(len(queue)!=1):
    for _ in range(K-1):
        queue.append(queue.popleft())
    answer+=(str(queue.popleft())+', ')
answer+=(str(queue.popleft())+'>')
print(answer)
