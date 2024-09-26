import sys
from collections import deque

N=int(sys.stdin.readline())
information=list(map(int,sys.stdin.readline().split()))




cur = [0 for _ in range(N)]
res = []
for _  in range(N): #고정할 위치
    for i in range(1,N+1):
        if(i not in res and cur[i-1] == information[i-1]):
            res.append(i)
            break
        else:
            cur[i-1]+=1


print(" ".join(map(str,res)))