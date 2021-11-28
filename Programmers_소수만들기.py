#Summer/Winter Coding(~2018)

from itertools import combinations 

def solution(nums):
    answer = 0
    temp = list(combinations(nums, 3))
    for i in temp: 
        s=sum(i)
        ck=-1
        for j in range(2,s):
            if(s%j==0):
                ck=1
                break
        if(ck==-1):
            answer+=1
    return answer