#1932번

import sys

n=int(sys.stdin.readline())
temp=[]
for i in range(n):
    a=[0]
    b=list(map(int,sys.stdin.readline().split()))
    temp.append(a+b+a)

for i in range(1,n):
    for j in range(1,i+2):
        temp[i][j]+=max(temp[i-1][j],temp[i-1][j-1])

print(max(temp[n-1]))