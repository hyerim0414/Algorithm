#240229
#큐
import sys
from collections import deque

N, K = list(map(int,sys.stdin.readline().split()))
queue=deque(range(1,N+1))

res=[]

while(len(queue)>0):
    for _ in range(K-1):
        queue.append(queue.popleft())
    res.append(queue.popleft())

print('<'+', '.join(list(map(str,res)))+'>')