#연습문제

def solution(n):
    ans=[]
    for i in range(1,n+1):
        if(n%i==0):
            ans.append(i)
    
        
    answer = sum(ans)
    return answer