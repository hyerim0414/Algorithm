#2108번

import sys

T=int(sys.stdin.readline())

N=[]
for _ in range(T):
    N.append(int(sys.stdin.readline()))

N=sorted(N)
mode=[[N[0],1]]
j=0
for i in range(1,T):
    if(mode[j][0]==N[i]):
        mode[j][1]+=1
    else:
        mode.append([N[i],1])
        j+=1

mode=sorted(mode,key=lambda x: x[1],reverse=True)
print(round(sum(N)/T))
print(N[T//2])
if(len(mode)>1):
    print(mode[0][0] if( mode[0][1]!= mode[1][1]) else mode[1][0])
else:
    print(mode[0][0])
print(max(N)-min(N))