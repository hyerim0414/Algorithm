'''
24.11.19

- deque에 rotate() 함수 활용 (1->오른쪽으로 밀어짐, -1 -> 왼쪽으로 밀어짐)
- 회전하는 큐 세가지 연산

1) 원소 뽑기 (제일 앞) => popleft()
2) 왼쪽으로 이동 => rotate(-1)
3) 오른쪽으로 이동 => rotate(1)

- 원하는 원소를 뽑기위한 2,3)번 연산의 최소값을 출력
- 순서대로 뽑아야함
- dfs처럼 계속 파고들어가야할 것 같음 
- 다른 사람 풀이에서는 index() 함수를 이용하여 위치를 알아내고 절반이하 => 왼쪽, 그렇지 않으면 => 오른쪽으로 밀어냄 
- 다음엔 index() 함수를 사용해볼 것
'''

import sys
from collections import deque
import copy

N, M = list(map(int,sys.stdin.readline().split()))
num_L = list(map(int,sys.stdin.readline().split()))

queue = deque([i for i in range(1,N+1)])
res = 0
for num in num_L:
    if(queue[0] == num):
        queue.popleft()
        continue
    tmp_L = copy.deepcopy(queue) 
    tmp_R = copy.deepcopy(queue)
    count_l = 0
    count_r = 0
    while True: 
        tmp_L.rotate(-1)
        count_l +=1
        if(tmp_L[0] == num):
            tmp_L.popleft()
            break

    while True: 
        tmp_R.rotate(1)
        count_r +=1
        if(tmp_R[0] == num):
            tmp_R.popleft()
            break
    
    res += min(count_l, count_r)
    queue = copy.deepcopy(tmp_R)

print(res)

        
