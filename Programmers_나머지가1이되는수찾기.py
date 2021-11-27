#월간 코드 챌린지 시즌3

def solution(n):
    answer = 0
    for i in range(2,n):
        if((n-1)%i==0):
            answer=i
            break
    return answer