#해시

def solution(participant, completion):
    answer=""
    dic_par={}
    len_par=len(participant)
    sum_com=0
    sum_par=0
    for i in range(len_par):
        dic_par[str(hash(participant[i]))]=participant[i]
        sum_par+=hash(participant[i])
    #print(dic_par)
    for i in range(len_par-1):
        sum_com+=hash(completion[i])
    answer=dic_par[str(sum_par-sum_com)]
    return answer