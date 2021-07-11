'''
- A는 오름차순 정렬, B는 내림차순 정렬
'''
def solution(A,B):
    answer = 0
    A=sorted(A)
    B=sorted(B,reverse=True)
    for i in range(len(A)):
        answer+=A[i]*B[i]
    return answer