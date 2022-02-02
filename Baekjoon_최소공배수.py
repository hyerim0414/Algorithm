#1934번

import sys
import math
T= int(sys.stdin.readline())

def lcm(a,b):
    g=math.gcd(a,b)
    return a*b//g

for _ in range(T):
    a,b=map(int,sys.stdin.readline().split())
    print(lcm(a,b))
