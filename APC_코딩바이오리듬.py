#2021-APC-div2

'''
- 정렬 후 작은 값 search
-출처: https://vhxpffltm.tistory.com/146
'''

import sys
import math

birth=sys.stdin.readline()
n=int(sys.stdin.readline())
day=[sys.stdin.readline()[:-1] for _ in range(n)]
day=sorted(day)
good=[]

def Count(L):
    multi=1
    temp=0
    for i in range(8): 
        temp+=math.pow(int(birth[i])-int(L[i]),2)
        if(i==3 or i==5 or i==7):
            multi*=temp
            temp=0
    good.append([multi,L])
    return

for i in range(n):
    Count(day[i])

good=sorted(good,key=lambda x: (x[0]),reverse=True)
print(good[0][1])