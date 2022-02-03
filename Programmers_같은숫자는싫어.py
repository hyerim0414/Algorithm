#연습문제

from collections import deque

def solution(arr):
    answer = []
    q=deque(arr)
    while(q):
        if(len(q)==1 or q[0]!=q[1]):
            answer.append(q.popleft())
        else:
            q.popleft()
    return answer
