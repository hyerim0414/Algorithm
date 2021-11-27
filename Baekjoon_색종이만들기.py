#2630번

import sys

N = int(sys.stdin.readline())
p = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

result = []

def Paper(x, y, N) :
  color = p[x][y]
  for i in range(x, x+N) :
    for j in range(y, y+N) :
      if color != p[i][j] :
        Paper(x, y, N//2)
        Paper(x, y+N//2, N//2)
        Paper(x+N//2, y, N//2)
        Paper(x+N//2, y+N//2, N//2)
        return
  if color == 0 :
    result.append(0)
  else :
    result.append(1)


Paper(0,0,N)
print(result.count(0))
print(result.count(1))