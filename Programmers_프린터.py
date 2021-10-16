#스택/큐

def solution(priorities, location):
    count=0
    max_importance=max(priorities)
    while(1):
        if(max_importance==priorities[0]):
            if(location==0):
                return(count+1)
            priorities.pop(0)
            count+=1
            location-=1
            max_importance=max(priorities)
        else:
            if(location==0):
                location=len(priorities)
            priorities.append(priorities.pop(0))
            location-=1