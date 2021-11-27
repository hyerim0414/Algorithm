#힙(Heap)

def solution(scoville, K):
    import heapq
    #heap=[]
    heap=scoville
    count=0
    heapq.heapify(heap) #알아서 min heap 구조로 들어감
    
    while(1):
        if(len(heap)==1 and heap[0]<K ):  #heapq.heappop <K 할 시 오류
            return -1
        if(heap[0]>=K): #heap의 맨앞은 항상 최소값
            break
        a=heapq.heappop(heap)
        b=heapq.heappop(heap)
        heapq.heappush(heap,a+2*b)
        count+=1
    return count