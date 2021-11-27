#정렬

def solution(citations):
    res_key=0
    for key in range(max(citations)):
        k=list(map(lambda x: x>=key, citations)).count(True)
        if(k>=key and (len(citations)-k)<=key and res_key<key):
            res_key=key
    return res_key