#해시

def solution(clothes):
    ans=1
    choice_num={}
    for i in range(len(clothes)):
        if clothes[i][1] in choice_num:
            choice_num[clothes[i][1]]+=1
        else:
            choice_num[clothes[i][1]]=1
    for i in choice_num.values():
        ans*=(i+1)
    return ans-1