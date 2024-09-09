
'''
공식 정육면체는 모든 면이 맞닿아있음
가운데부터 층수를 계산하면 그 층에 있는 숫자는 항상 최소 층수값으로 이동가능
1개, 6개, 12개, 24개, 48개,... 무슨 수열같은데 이름이 기억안남
S1=1
S_n= S_(n-1)+6*(n-1), n>1
'''

import sys

N=int(sys.stdin.readline())

cnt=1
res=1
while(N>res):
   res+=6*cnt
   cnt+=1
print(cnt)