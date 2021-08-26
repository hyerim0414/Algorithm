#1520번

import sys

M,N = map(int,sys.stdin.readline().split())

m = [list(map(int, input().split())) for _ in range(M)]
mem = [[-1]*N for _ in range(M)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if (x == M-1 and y == N-1): #끝
        return 1
    if mem[x][y] != -1: #이미 방문해본 곳
        return mem[x][y]
    mem[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < M and 0 <= ny < N):
            if (m[nx][ny] < m[x][y]):
                mem[x][y] += dfs(nx, ny)
    return mem[x][y]

print(dfs(0, 0))