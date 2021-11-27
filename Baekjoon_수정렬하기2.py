#2751번

import sys

T=int(sys.stdin.readline())
N=[]
for _ in range(T):
    N.append(int(sys.stdin.readline()))
sort_N=sorted(N)
for i in sort_N:
    print(i)