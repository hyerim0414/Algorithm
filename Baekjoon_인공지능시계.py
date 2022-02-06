#2530번

import sys

h,m,s=map(int,sys.stdin.readline().split())
t=int(sys.stdin.readline().rstrip())

temp=s+t

s=(s+t)%60
temp=m+temp//60
m=temp%60
h=(h+temp//60)%24

print(h,m,s)