
import sys
from collections import deque

s=list(sys.stdin.readline().strip())

queue=deque(s)
wanted=sorted(s)

cnt=sum([ai==bi for ai,bi in zip(queue,wanted)]) #UB
if(s==wanted):
    print(0)
else:
    for _ in range(len(s)):
        queue.append(queue.popleft())
        tmp=sum([ai!=bi for ai,bi in zip(queue,wanted)])
 
        cnt=tmp if(tmp<cnt) else cnt
    print(cnt//2)



