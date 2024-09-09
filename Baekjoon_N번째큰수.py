
import sys
import heapq

N=int(sys.stdin.readline())

max_heap=[]

#다 저장하면 메모리 제한 문제 발생
for _ in range(N):
    items=list(map(int,sys.stdin.readline().split()))
    for item in items:
        tmp=item
        if (len(max_heap)==N):
            tmp=heapq.heappop(max_heap)
            tmp=item if item>tmp else tmp
        heapq.heappush(max_heap, tmp)

print(heapq.heappop(max_heap))
