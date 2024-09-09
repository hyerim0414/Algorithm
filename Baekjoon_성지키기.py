import sys

N,M = list(map(int,sys.stdin.readline().strip().split()))

R=set([])
C=set([])

for i in range(N):
    row=sys.stdin.readline().strip()
    for j in range(M):
        if(row[j]=='X'):
            R.add(i)
            C.add(j)

print(max(N-len(R),M-len(C)))
