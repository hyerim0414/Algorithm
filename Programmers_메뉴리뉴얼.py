#2021 KAKAO BLIND RECRUITMENT

from itertools import combinations

def solution(orders, course):
    
    res=[]
    for c in course:
        combo={}
        for o in orders:
            combi = list(map(''.join, list(combinations(sorted(o), c))))
            for com in combi:
                if(com in combo):
                    combo[com]+=1
                else:
                    combo[com]=1
        if(len(combo)==0):
            continue
        max_com=max(combo.values())   
        for key,item in combo.items():
            if(item>=2 and item==max_com):
                res.append(key)
    res=sorted(res)
    return res
