#힙(Heap)

#start로 이미 끝내준 일 제외시키기(중요)
def solution(jobs):
    import heapq
    T=0
    start=-1
    sum_time=0
    heap=[]
    finish=0
    while(finish<len(jobs)): #현재시간에서 요청할것 넣어주고 기다리는것들에서 짧은 거 빼주고
        for job in jobs:
            if(start<job[0]<=T):
                heapq.heappush(heap,[job[1],job[0]])
        if(heap==[]):
            T+=1
            continue
            
        work=heapq.heappop(heap)
        #각 일마다 걸린 시간
        if(T>work[1]):
            sum_time+=(T-work[1]+work[0])
        else :
            sum_time+=work[0]
        finish+=1
        start=T
        T+=work[0]

    answer=sum_time//len(jobs)
    return answer