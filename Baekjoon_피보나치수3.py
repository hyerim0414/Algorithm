#2749번
'''
- 메모리제이션 사용x(n이 크기 때문)
- 피사노주기 이용
- 주기의 길이가 P 일 때, N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M을 나눈 나머지와 같음
'''

import sys

n=int(sys.stdin.readline().rstrip())
mod=1000000
p=15*(mod//10)
fib=[0 for _ in range(p)]
fib[0]=0
fib[1]=1
for i in range(2, p):
    fib[i] = (fib[i-1]+fib[i-2])%mod

print(fib[n%p])