#15650번

from itertools import combinations
import sys

N,M=map(int,sys.stdin.readline().split())
combi=list(combinations(range(1,N+1),M))

for p in combi:
    print(*p)