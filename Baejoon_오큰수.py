import sys
from collections import deque

N= int(sys.stdin.readline())
A= list(map(int,sys.stdin.readline().strip().split()))

res=[]
queue=deque()

for idx, number in enumerate(A):
    if(len(queue)==0):
        queue.append((idx,number))
    else:
        while(len(queue)>0):
            cur_idx,cur_number = queue.pop()
            if(cur_number < number): 
                res.append((cur_idx,number))
            else:
                queue.append((cur_idx,cur_number))
                break
        queue.append((idx,number))

while(len(queue)>0):
    cur_idx,cur_number = queue.pop()
    res.append((cur_idx,-1))

res=sorted(res,key= lambda x: x[0])
answer=[x[1] for x in res]
print(" ".join(map(str,answer)))