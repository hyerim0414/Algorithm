#1697번

from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001
visited[n] = 1

def bfs():
    queue = deque()
    queue.append([n,0])
    while queue:
        cur,count = queue.popleft()
        if cur == k:
            return count
        for i in range(3):
            if i == 0:
                new = cur + 1
            elif i == 1:
                new = cur - 1
            else:
                new = cur * 2
            if new < 0 or new > 100000:
                continue
            if (visited[new]==0):
                queue.append([new,count+1])
                visited[new] = 1
    return count
print(bfs())
