#Summer/Winter Coding(~2018)

def solution(d, budget):
    answer=0
    d=sorted(d)
    nsum=0
    for i in range(len(d)):
        nsum+=d[i]
        if(nsum>budget):
            break
        answer += 1
    return answer