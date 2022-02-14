#1931번
'''
- 그리디 알고리즘
- 회의 시간이 짧은 것부터 선택 X -> 무조건 차이가 작다고 많은 회의 배정할 수 있는 것 아님
- 반례
 3
 1 10
 9 12
 11 20
 - 시작순으로 정렬, 자기 앞에 있는 회의 가능한지 카운팅
 - 시간 복잡도 O(nlogn)으로 줄이기 위해 끝시간-시작시간으로 정렬
'''

import sys

N=int(sys.stdin.readline())
meet=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

meet=sorted(meet,key=lambda x: (x[1],x[0]))
ct=1

lastT=meet[0][1]
for i in range(1,N):
    if(lastT<=meet[i][0]):
        lastT=meet[i][1]
        ct+=1
print(ct)