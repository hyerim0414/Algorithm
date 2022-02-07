#11401번
'''
- 보통 이항계수 문제는 nCk=n-1Ck-1+n-1Ck 로 풀지만 O(n^2)
- 정수론, 분할 정복 이용
- p가 소수이고, a와 p가 서로소일때 a^p-1=1 (mod p) ; Fermat's little thm
'''

import sys

n, k = map(int,sys.stdin.readline().split())
p = 1000000007

fac = [1 for _ in range(n+1)]

for i in range(2, n+1):
    fac[i] = fac[i-1] * i % p

def power(num,p,mod):
    if(p==1):
        return num%mod
    elif(p%2==1):
        return power(num,p//2,mod)**2*num%mod
    else:
        return power(num,p//2,mod)**2%mod

print(fac[n]*power(fac[k]*fac[n-k],p-2,p)%p)