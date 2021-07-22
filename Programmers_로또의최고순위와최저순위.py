def solution(lottos, win_nums):
    answer = []
    count=0
    for lotto in lottos:
        if(lotto in win_nums):
            count+=1
            
    if(count+lottos.count(0) <2):
        answer.append(6)
    else:
        answer.append(7-(count+lottos.count(0)))
    if(count <2):
        answer.append(6)
    else:
        answer.append(7-count)
    return answer