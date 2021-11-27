#10816번

import sys

def bi_search(start, end, find,L):
    mid=(start+end)//2
    if(start>end):
        return str(0)
    elif(L[mid]<find):
        return bi_search(mid+1,end,find,L)
    elif(L[mid]>find):
        return bi_search(start,mid-1,find,L)
    elif(L[mid]==find):
        count=1
        left,right=mid-1,mid+1
        while(start<=left and L[left]==find):
            left-=1
            count+=1
        while(right<=end and L[right]==find):
            right+=1
            count+=1
        return str(count)
    


N= int(sys.stdin.readline())
L = sorted(list(map(int,sys.stdin.readline().split())))
M= int(sys.stdin.readline())
F=list(map(int,sys.stdin.readline().split()))

answer=''
for i in F:
    answer+=bi_search(0,N-1,i,L)+' '
print(answer)