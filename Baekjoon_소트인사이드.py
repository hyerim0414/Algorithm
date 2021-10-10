#1427번

import sys

T=sys.stdin.readline()
N=[int(T[i]) for i in range(len(T)-1)]
N=sorted(N,reverse=True)
for n in N:
    print(n,end='')
