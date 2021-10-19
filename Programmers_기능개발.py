#스택/큐

def solution(progresses, speeds):
    import math
    answer = []
    front=-1
    rear=0
    que=[math.ceil((100-progresses[0])/speeds[0])]
    count=1
    for i in range(1,len(progresses)):
        days=math.ceil((100-progresses[i])/speeds[i])
        if(que[front+1]<days):
            answer.append(count)
            front=rear
            count=0
        que.append(days)
        rear+=1
        count+=1
    if(count>0):
        answer.append(count)
    return answer