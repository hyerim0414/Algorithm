#1021번
import sys
from collections import deque

N,M= map(int,sys.stdin.readline().split())
data = deque(range(1,N+1))
index = list(map(int,sys.stdin.readline().split()))

count = 0
for n in index:
    while(True):
        if (data[0] == n):
            data.popleft()
            break
        else:  
            if (data.index(n) <= len(data)//2):
                data.rotate(-1) #왼쪽으로 1만큼 회전 1 2 3 => 2 3 1
                count += 1
            else:
                data.rotate(1)
                count += 1

print(count)