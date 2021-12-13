#1037번

import sys
import math

N=int(sys.stdin.readline())
num=list(map(int,sys.stdin.readline().split()))
num=sorted(num)

print(num[0]*num[-1])
