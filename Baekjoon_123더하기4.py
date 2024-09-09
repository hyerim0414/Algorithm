#DP를 이용한건 어느정도 맞았는데 처음에 list를 3개나 만들고 반복문 중첩해서 시간초과... 

import sys

T=int(sys.stdin.readline())

res=[1+i//2 for i in range(10001)]

for i in range(3,10001):
    res[i]+=res[i-3]
for _ in range(T):
    n=int(sys.stdin.readline())
    print(res[n])