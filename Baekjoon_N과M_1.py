#15649번

from itertools import permutations
import sys

N,M=map(int,sys.stdin.readline().split())
permu=list(permutations(range(1,N+1),M))

for p in permu:
    print(*p)