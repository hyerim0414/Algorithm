#1655번
'''
- 힙을 두개를 만들어서 가운데 값 찾기
- 왼쪽 힙은 max heap, 오른쪽 힙은 min heap을 사용
- 중앙값은 항상 left heap의 최댓값
'''

import sys
import heapq

N= int(sys.stdin.readline())
heap1=[]
heap2=[]
count=1
num= int(sys.stdin.readline())
heapq.heappush(heap1,(-num,num))
print(num)

for _ in range(N-1):
    num= int(sys.stdin.readline())
    if(count%2==0):
        heapq.heappush(heap1,(-num,num))
    else: # 두 힙에서 뽑은 값 중 작은 값 
        heapq.heappush(heap2,num)
    
    if(heap1[0][1]>heap2[0]):
        h1=heapq.heappop(heap1)[1]
        h2=heapq.heappop(heap2)
        heapq.heappush(heap1,(-h2,h2))
        heapq.heappush(heap2,h1)
    print(heap1[0][1])
    count+=1
    