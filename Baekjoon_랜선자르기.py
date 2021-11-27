#1654번
'''
- 자를 수 있는 최대 랜선길이 찾기
'''
import sys

def bi_search(start, end, K_list,N):
    mid=(start+end)//2
    if(start>end):
        return end
    
    count=0
    for n in K_list:
        count+=(n//mid) #mid 길이로 잘랐을 때 얻을 수 있는 wire 개수
    
    if(count<N):
        end-=1
        return bi_search(start,mid-1,K_list,N)

    elif(count>=N):
        return bi_search(mid+1,end,K_list,N)
    

K, N= map(int,sys.stdin.readline().split())
K_list=[]
for _ in range(K):
    K_list.append( int(sys.stdin.readline()))

print(bi_search(1,max(K_list),K_list,N))
