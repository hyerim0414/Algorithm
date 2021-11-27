#2021 KAKAO BLIND RECRUITMENT

def solution(new_id):
    answer = ''
    #rule='abcdefghijklnmopqrstuvwxyz-_.'
    new_id=new_id.lower()
    
    for ch in new_id:
        if(ch.isalnum() or ch in '-_.'):
            answer+=ch

    while('..' in answer):
        answer=answer.replace('..','.')
    if(answer[0]=='.'and len(answer)>1):
        answer=answer[1:]
    if(answer[-1]=='.'):
        answer=answer[:-1]
    if(answer==''):
        answer='a'
    if(len(answer)>=16):
        answer=answer[0:15]
        if(answer[-1]=='.'):
            answer=answer[:-1]
    if(len(answer)<3):
        answer+=answer[-1]*(3-len(answer))
        
    return answer