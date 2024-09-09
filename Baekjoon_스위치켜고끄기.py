
def switch_change(value):
    if value==1:
        return 0
    else:
        return 1

import sys
N=int(sys.stdin.readline())

switch=[0]+list(map(int,sys.stdin.readline().split()))

m=int(sys.stdin.readline())

for _ in range(m):
    gender, location=list(map(int,sys.stdin.readline().split()))
    if(gender==1):
        tmp=location
        while(tmp<=N):
            switch[tmp]= switch_change(switch[tmp])
            tmp+=location
    else:
        ck=min(location-1,N-location)
        switch[location] = switch_change(switch[location])
        for i in range(1,ck+1):
            if(switch[location-i]==switch[location+i]):
                switch[location-i]= switch_change(switch[location-i])
                switch[location+i]= switch_change(switch[location+i])
            else:
                break

i=0
if(N<=20):
    print(' '.join(map(str,switch[1:])))
else:
    while(i+20<=N):
        print(' '.join(map(str,switch[1+i:1+i+20])))
        i+=20
    if(N%20!=0):
        print(' '.join(map(str,switch[1+i:])))