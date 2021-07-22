def solution(n, lost, reserve):
    for i in range(1,n+1):
        if(i in lost and i in reserve):
            lost.remove(i)
            reserve.remove(i)
        
    ans = n-len(lost)
    for i in lost:
        if (i-1 in reserve):
            k=i-1
        elif (i+1 in reserve):
            k=i+1
        else:
            continue
        reserve.remove(k)
        ans+=1
    return ans