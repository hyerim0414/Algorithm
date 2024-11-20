'''
24/11/20

- 시간 제한 1초 -> O(N)에서 끝낼 수 있게 최적화 중요
- 블로그 시작 N일, X일에 대해 가장 많이 들어온 방문자 수와 기간 개수
- 최대 방문자가 0이면 => SAD 출력
'''

import sys

N, X = list(map(int,sys.stdin.readline().split()))
visitor = list(map(int,sys.stdin.readline().split()))

tmp = sum(visitor[:X])

max_visit = tmp
max_count = 1

for i in range(N-X):
    j = i+X
    tmp = tmp - visitor[i] + visitor[j]
    if(tmp == max_visit):
        max_count+=1
    elif(tmp> max_visit):
        max_visit = tmp
        max_count = 1

if(max_visit==0):
    print("SAD")
else:
    print(max_visit)
    print(max_count)
