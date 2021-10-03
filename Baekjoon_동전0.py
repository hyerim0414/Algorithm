#11047번

import sys

n,k=map(int,sys.stdin.readline().split())
coin=[int(sys.stdin.readline()) for _ in range(n)]
coin=sorted(coin,reverse=True)
for i in range(n):
    if(coin[i]<=k):
        coin=coin[i:]
        break
    
def findCoin(id,cur,k,count):
    if(cur==k):
        return count
    else:
        for i in range(id,len(coin)):
            if((k-cur)>=coin[i]):
                temp=(k-cur)//coin[i]
                count=findCoin(i+1,cur+temp*coin[i],k,count+temp)
                return count


print(findCoin(0,0,k,0))