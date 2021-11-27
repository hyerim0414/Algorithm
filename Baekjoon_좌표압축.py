#18870번
'''
- set을 이용하여 중복 없애준 뒤 list.index() 를 이용하면 시간복잡도 O(N)를 갖게 됨 
- dictionary를 이용하면 index에 O(1)안에 접근 가능
'''
import sys

T=int(sys.stdin.readline())
N=list(map(int,sys.stdin.readline().split()))
S=sorted(set(N))
dic={S[i]:i for i in range(len(S))}
for n in N:
    print(dic[n],end=" ")