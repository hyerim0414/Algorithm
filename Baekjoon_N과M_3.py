#15651번

from itertools import product
import sys

N,M=map(int,sys.stdin.readline().split())
prod=list(product(range(1,N+1),repeat=M))

for p in prod:
    print(*p)