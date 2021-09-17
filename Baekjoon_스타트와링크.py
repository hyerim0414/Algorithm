#14889번
#삼성 SW 역량 테스트 기출 문제 2
'''
- itertools 적극적으로 활용
'''

import sys 
from itertools import combinations

N=int(sys.stdin.readline())
skill=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
cases=list(combinations(range(N),N//2))
min_res=99

for st in cases:
    li=[i for i in range(N) if i not in st]
    st_sum,li_sum=0,0
    for i,j in zip(st,li):
        for k,l in zip(st,li):
            st_sum+=(skill[i][k])
            li_sum+=(skill[j][l])
    min_res=abs(st_sum-li_sum) if(abs(st_sum-li_sum)<min_res) else min_res

print(min_res)