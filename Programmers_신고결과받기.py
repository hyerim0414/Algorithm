#2022 KAKAO BLIND RECRUITMENT

def solution(id_list, report, k):
    id={i:set() for i in id_list} #{신고받은사람:set(신고한사람들)}
    stop_ct={i:0 for i in id_list} # 신고 받아들여진 횟수 카운팅

    #print(id)
    for s in report:
        call,target=s.split()
        id[target].add(call) 
    
    for i in id:
        if(len(id[i])>=k):
            for j in id[i]:
                stop_ct[j]+=1
    
    return list(stop_ct.values())






solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)