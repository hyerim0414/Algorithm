#2231번

import sys 

N=int(sys.stdin.readline())
ck=0
creat=str(1)

while(int(creat)<N):
    temp=int(creat)
    for i in creat:
        temp+=int(i)
    #print(creat, temp)
    if(temp==N):
        ck=1
        break
    else:
        creat=str(int(creat)+1)

print(creat) if (ck==1) else print(0)