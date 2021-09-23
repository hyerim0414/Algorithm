#7562번

from collections import deque

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]

def bfs(curX, curY, wantX, wantY):
    queue = deque()
    queue.append((curX,curY))
    while queue:
        cur_x, cur_y = queue.popleft()
        if cur_x == wantX and cur_y == wantY:
            print(visited[cur_x][cur_y] - 1)
            return True
        for i in range(8):
            new_x = cur_x + dx[i]
            new_y = cur_y + dy[i]
            if new_x < 0 or new_x >= l or new_y < 0 or new_y >= l:
                continue
            if visited[new_x][new_y] == 0:
                visited[new_x][new_y] = visited[cur_x][cur_y] + 1
                queue.append((new_x, new_y))

    return False


n = int(input())
for _ in range(n):
    l = int(input())
    visited = [[0] * l for _ in range(l)]
    cur_x, cur_y = map(int, input().split())
    want_x, want_y = map(int, input().split())
    visited[cur_x][cur_y] = 1
    bfs(cur_x, cur_y, want_x, want_y)