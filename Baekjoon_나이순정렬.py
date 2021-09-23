#10814번

import sys

T=int(sys.stdin.readline())
N=[sys.stdin.readline().split() for _ in range(T)]
N=sorted(N,key=lambda x: (int(x[0])))

for i in range(T):
    print(*N[i])