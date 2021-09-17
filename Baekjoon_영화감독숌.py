#1436번

import sys

N=int(sys.stdin.readline())
count=1
num=666
while(True):
    if(count==N):
        break
    num+=1
    if('666' in str(num)):
        count+=1
    
print(num)
