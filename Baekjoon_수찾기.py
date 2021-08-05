#1920번

import sys

def bi_search(start, end, find,L):
    mid=(start+end)//2
    if(start>end):
        return 0
    elif(L[mid]<find):
        return bi_search(mid+1,end,find,L)
    elif(L[mid]>find):
        return bi_search(start,mid-1,find,L)
    elif(L[mid]==find):
        return 1
    

N= int(sys.stdin.readline())
L = sorted(list(map(int,sys.stdin.readline().split())))
M= int(sys.stdin.readline())
F=list(map(int,sys.stdin.readline().split()))

for i in F:
    print(bi_search(0,N-1,i,L))