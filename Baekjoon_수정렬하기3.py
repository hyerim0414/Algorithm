#10989번
'''
- 카운팅 이용
'''

import sys

T=int(sys.stdin.readline())

count_List=[0]*100000
for _ in range(T):
    num=int(sys.stdin.readline())
    count_List[num]+=1
    
for i in range(100000):
    while(count_List[i]!=0):
        count_List[i]-=1
        print(i)

