'''
- 이분탐색
'''
def solution(n, times):
    answer = 0
    times=sorted(times)
    left,right=0,times[-1]*n
    while(left<=right):
        mid=(left+right)//2
        available_num=0
        for i in times:
            available_num+=mid//i
        if(available_num>=n):
            answer=mid
            right=mid-1
        else:
            left=mid+1
            
        
    return answer