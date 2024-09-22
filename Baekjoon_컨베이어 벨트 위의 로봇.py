# 240922

import sys
from collections import deque

N, K = map(int,sys.stdin.readline().split())
A = deque(list(map(int,sys.stdin.readline().split())))
robot = deque([False for _ in range(N)]) # 로봇 위치

i=1
while(True):
    # 1. 벨트 회전
    A.rotate(1)
    robot.rotate(1)

    # 2. 로봇 회전
    robot[N-1] = False # 내리는 위치에 도달하면 즉시 내림
    for cur_r in range(N-2,-1,-1):
        if(robot[cur_r] and A[cur_r+1]>0 and not robot[cur_r+1]):
            robot[cur_r],robot[cur_r+1] = False, True
            A[cur_r+1] -= 1
            
    robot[N-1] = False # 내리는 위치에 도달하면 즉시 내림

    # 3. 로봇 올리기
    if(A[0]>0):
        A[0]-=1
        robot[0]= True

    # 다음 단계 넘어가기 전 break 조건 체크
    if(A.count(0)>=K): # 여러개가 0이 되어서 한 단계에서 k초과가 되는 경우 있을 수 있음! ==K -> >=K 로 수정
        print(i)
        break
    else:
        i+=1

