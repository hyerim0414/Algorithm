#1927번
'''
- min heap 은 루트 노드에 최소값을 가진다.
- 부모 노드(i)의 자식 노드(2i+1,2i+2)는 부모 노드보다 값이 크다.
'''

import sys
import heapq

N= int(sys.stdin.readline())
heap=[]
for _ in range(N):
    num= int(sys.stdin.readline())
    if(num==0):
        if(heap):
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,num)