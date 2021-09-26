#2110번

import sys

def d_count(distance,homes):
    count=1
    current_home=homes[0]
    for h in homes[1:]:
        if(current_home+distance <=h): #지켜야 할 최소 거리보다 다음 집이 멀리 있으면, 설치가능
            count+=1
            current_home=h
    return count  

N,C= map(int,sys.stdin.readline().split())

homes=sorted([int(sys.stdin.readline()) for _ in range(N)])

# homes[-1]-homes[0] : 최대 거리

def bi_search(start,end,homes,C,ans):
    distance=(start+end)//2
    if(start>end):
        return ans
    if(d_count(distance,homes)<C): #최소거리 줄이기
        return bi_search(start,distance-1,homes,C,ans)
    else: #최소거리를 더 늘려보기
        return bi_search(distance+1,end,homes,C,distance)

print(bi_search(1,homes[-1]-homes[0],homes,C,0))
