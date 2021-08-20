#1904번

import sys

T=[0,1,2,3]
N=int(sys.stdin.readline())

if(len(T)<=N):
    for i in range(len(T),N+1):
        T.append((2*T[i-2]+T[i-3])%15746)
print(T[N])