'''
- DP문제 : 작은 문제로 쪼개서 풀기 
- land에 이전행의 최댓값을 더해가면서, 가능한 경우중에서 좋은 경우만을 남기도록
'''

def solution(land):
    for i in range(1,len(land)):
        for j in range(len(land[0])):
            land[i][j]+=max(land[i-1][:j]+land[i-1][j+1:])
    return max(land[len(land)-1])