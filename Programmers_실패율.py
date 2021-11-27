#2019 KAKAO BLIND RECRUITMENT

def solution(N, stages):
    answer = []
    res={}
    p=len(stages)
    for stage in range(1,N+1):
        if(p==0):
            res[stage]=0
            continue
        res[stage]=stages.count(stage)/p
        p-=stages.count(stage)
        
    return sorted(res,key=lambda x:res[x],reverse=True)