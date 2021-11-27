#찾아라 프로그래밍 마에스터

def solution(nums):
    n=len(nums)//2
    nums=set(nums)
    return min(n,len(nums))