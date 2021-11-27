#15652번

from itertools import combinations_with_replacement
import sys

N,M=map(int,sys.stdin.readline().split())
combi_rep=list(combinations_with_replacement(range(1,N+1),M))

for p in combi_rep:
    print(*p)