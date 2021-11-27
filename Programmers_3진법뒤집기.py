#월간 코드 챌린지 시즌1

import math
def solution(n):
    answer = 0
    num=''
    while(n>0):
        num=str(n%3)+num
        n=n//3
    for i,ch in enumerate(num):
         answer+=int(ch)*math.pow(3,i)
    return answer