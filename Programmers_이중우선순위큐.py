#힙(Heap)

import heapq
def solution(operations):
    answer = []
    heap=[]
    
    
    for op in operations:
        if op.startswith("I"):
            heapq.heappush(heap, int(op[2:]))
            continue
        if(heap!=[]): #빈큐 삭제요청시 무시
            if op=="D -1":
                heapq.heappop(heap)
            else:
                max_heap=[]
                for num in heap:
                    heapq.heappush(max_heap,[-num,num])
                i=heapq.heappop(max_heap)
                heap.remove(i[1])
    if(heap==[]):
        return [0,0]
    elif(len(heap)==1):
        return [heap[0],heap[0]]
    else:
        min_num=heapq.heappop(heap)
        max_heap=[]
        for num in heap:
                heapq.heappush(max_heap,[-num,num])
        max_num=heapq.heappop(max_heap)
        return [max_num[1],min_num]