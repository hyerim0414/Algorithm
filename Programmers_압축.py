#2018 KAKAO BLIND RECRUITMENT

from string import ascii_uppercase
def solution(msg):
    answer = []
    #초기 설정
    dict={}
    for idx, c in enumerate(list(ascii_uppercase)):
        dict[c]=idx+1
    last_idx=27
    c=1
    w=0
    # msg[w:c+1] 가 없으면 msg[w:c] 해당 번호 출력 & msg[w:c+1] 새로 등록
    while(c!=len(msg)):
        if(msg[w:c+1] in list(dict.keys())):
            c+=1
            continue
        answer.append(dict[msg[w:c]])
        dict[msg[w:c+1]]=last_idx
        last_idx+=1
        w=c
        c+=1
    answer.append(dict[msg[w:c]])       
    return answer