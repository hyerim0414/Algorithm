#11054번

import sys

T=int(sys.stdin.readline())

dp_up=[1 for _ in range(T)]
dp_down=[1 for _ in range(T)]
seq=list(map(int,sys.stdin.readline().split()))
reverse_seq=seq[::-1]

for i in range(T):
    for j in range(i):
        if(seq[i]>seq[j] ):
            dp_up[i]=max(dp_up[i],dp_up[j]+1)
        if(reverse_seq[i]>reverse_seq[j] ):
            dp_down[i]=max(dp_down[i],dp_down[j]+1)


dp=[]
for i in range(T):
    dp.append(dp_down[T-1-i]+dp_up[i]-1)

print(max(dp))
