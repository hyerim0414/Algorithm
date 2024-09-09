#24.02.29
#큐
#Valueerror 테스트케이스 : 모두 동일한 값일때
import sys
from collections import deque

T=int(sys.stdin.readline())

for _ in range(T):
    res=1
    N,M = list(map(int,sys.stdin.readline().split()))
    impotrance= list(map(int,sys.stdin.readline().split()))
    queue=deque([l for l in enumerate(impotrance)])
    while(res<=N):   
        idx, value=queue.popleft()
        if(res==N):
            print(res)
            break
        tmp=max(queue,key=lambda x: x[1])[1]
        if((idx==M) & (value>=tmp)):
            print(res)
            break
        elif(value>=tmp):
            res+=1
            continue
        else:
            queue.append((idx, value))
        

