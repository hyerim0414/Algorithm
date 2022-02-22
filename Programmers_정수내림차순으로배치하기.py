#연습문제

def solution(n):
    ans=0
    num=list(map(int,str(n)))
    num=sorted(num,reverse=True)
    for i in range(len(num)):
        ans+=(10**i*num[-(i+1)])
    return ans