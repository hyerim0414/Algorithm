#스택/큐

def solution(prices):
    answer=[] 
    N=len(prices)
    for i in range(N):
        count=0
        for j in range(i+1,N):  
            if(prices[i]<=prices[j]): 
                count+=1
            else:
                count+=1
                break
 
        answer.append(count)
    return answer