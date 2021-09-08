#9663번

import sys

N=int(sys.stdin.readline())
count=0

def NQ(nq,count):
    if(len(nq)==N):
        return count+1
    
    else:
        for i in range(N):
            if(nq==[]):
                count=NQ([i],count)
            elif(abs(nq[-1]-i)!=1 and (i not in nq)):
                ck=0
                for j in range(len(nq)):
                    if(abs(nq[j]-i)==(len(nq)-j)):
                        ck=-1
                        break
                if(ck==0) :
                    count=NQ(nq+[i],count) 

        return count

print(NQ([],0))           