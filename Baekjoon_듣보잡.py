'''
24/11/19
- 듣도 못한 명단 N
- 보도 못한 명단 M
- 듣도 보도 못한 명단을 구하는
N과 m의 모두 포함되는 (교집합)

'''
import sys
N, M = list(map(int,sys.stdin.readline().split()))

l1 = set([sys.stdin.readline()[:-1] for _ in range(N)])
l2 = set([sys.stdin.readline()[:-1] for _ in range(M)])

res = sorted(l1.intersection(l2))
print(len(res))
print(*res,sep="\n")