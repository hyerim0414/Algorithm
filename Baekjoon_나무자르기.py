#2805번

import sys

def bi_search(start,end,tree_length,M):
    mid=(start+end)//2
    if(start>end):
        return end
    
    count=0
    for tree in tree_length:
        if(tree>mid): #잘린 나무 길이
            count+=(tree-mid)  
    
    if(count<M):
        return bi_search(start,mid-1,tree_length,M)

    elif(count>=M):
        return bi_search(mid+1,end,tree_length,M)
    

N,M= map(int,sys.stdin.readline().split())
tree_length=list(map(int,sys.stdin.readline().split()))

print(bi_search(0,max(tree_length),tree_length,M))
