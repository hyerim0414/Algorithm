#9184번
'''
- memoization 이용
'''

import sys

mem=[[[0 for _ in range(21)] for _ in range(21)]for _ in range(21)]
mem[0][0][0]=1

def w(a,b,c):
    if (a <= 0 or b <= 0 or c <= 0):
        return 1
    if (a > 20 or b > 20 or c > 20):
        return w(20,20,20)

    if mem[a][b][c]:
         return mem[a][b][c]

    if( a < b < c):
        mem[a][b][c]= w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return mem[a][b][c]
    else:
        mem[a][b][c]= w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return mem[a][b][c]
while(True):
    a, b, c=map(int,sys.stdin.readline().split())
    if(a==b==c==-1):
        break
    print('w({}, {}, {}) = {}'.format(a,b,c,w(a,b,c)))

