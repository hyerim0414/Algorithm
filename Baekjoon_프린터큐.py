'''
24.11.19

- 현재 문서보다 중요도 높은 문서가 한 개라도 있으면 제일 뒤로 이동, 그렇지 않으면 인쇄
- 즉, index 위치보다 중요도에 따라 인쇄
- 중요도에 따라 정렬 후, 각 원소 위치 count 하면 될 것 같음 => 이렇게 되면 중요도 동일한 값들 떄문에 순차적으로 빼내는게 아니게 됨
- M 은 index의미
- 중요도 정렬 후 deque -> 해당 값이 나가면, 중요도에서도 out, 동일 중요도만 남으면 이제 원하는 index까지 out시키기


'''

import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = list(map(int,sys.stdin.readline().split()))
    tmp = list(map(int,sys.stdin.readline().split()))
    impt_L = deque(sorted(tmp, reverse=True))
    num_L = deque([(idx,importance) for idx,importance in enumerate(tmp)])

    count = 0
    while True:
        idx, num = num_L[0]
        if(num == impt_L[0]):
            num_L.popleft()
            impt_L.popleft()
            count+=1
            if(idx == M):
                print(count)
                break
        else:
            num_L.rotate(-1)