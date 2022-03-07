#연습문제

def solution(strings, n):
    strings=sorted(strings)
    answer=sorted(strings, key=lambda x: x[n])
    return answer