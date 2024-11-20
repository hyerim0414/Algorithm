'''
24/11/20 (해결x- 해당 코드는 메모리 초과)
- N줄에 0~9 이하 숫자가 세개씩
- 처음 세 개 중 하나를 골라 시작
- 바로 아래 (1,0) 또는 그 옆 대각선 (1,-1)or(1,1) / 이때 board 경계를 넘어가지 않도록 주의
=> 3개밖에 안되니까 수기로 처리
- 이때 얻을 수 있는 최대 점수, 최소 점수를 구하여라 (DP) => 메모리 초과
- 미리 input을 다 받지 말고 하나씩 받기
- DP + 슬라이싱 윈도우 활용
'''
import sys
from collections import deque

N = int(sys.stdin.readline())

board = deque([list(map(int,sys.stdin.readline().split())) for _ in range(N)])
min_board = deque([[9*N,9*N,9*N] for _ in range(N)])
max_board = deque([[0,0,0] for _ in range(N)])

dmove = [(1,0), (1,1), (1,-1)]

for cy in range(3):
    min_board[0][cy] = board[0][cy]
    max_board[0][cy] = board[0][cy]

for cur_line in range(N-1):
    for cy in range(3):
        for dx,dy in dmove:
            next_line, ny = cur_line+dx, cy+dy
            if(0<= ny < 3):
                min_board[next_line][ny] = min(min_board[next_line][ny], min_board[cur_line][cy] + board[next_line][ny])
                max_board[next_line][ny] = max(max_board[next_line][ny], max_board[cur_line][cy] + board[next_line][ny])

print(*[max(max_board[N-1]), min(min_board[N-1])])
