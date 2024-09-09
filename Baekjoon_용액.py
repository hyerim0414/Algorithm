import sys

N=int(sys.stdin.readline())

case=list(map(int,sys.stdin.readline().split()))

res=2000000000
x=[0,0]

l=sorted([(abs(item),item) for item in case])


for i in range(len(case)-1):
    tmp=abs(l[i][1]+l[i+1][1])
    if (tmp<res):
        res=tmp
        x=[l[i][1], l[i+1][1]]

print(' '.join(map(str,sorted(x))))

