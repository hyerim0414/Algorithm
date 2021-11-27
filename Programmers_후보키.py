#2019 KAKAO BLIND RECRUITMENT
'''
- sort 후 인접 원소들과 비교하여 uniqueness 판단
- set을 이용하여 갯수파악
'''

from itertools import combinations
def solution(relation):
    answer = 0
    feature, len_id=len(relation[0]),len(relation)
    find=[]
    i=1

    while(i<=len_id):
        for k in combinations(range(len(relation[0])),i):
            key_list=set()
            for i in range(len_id):
                temp=''
                for j in k:
                    temp+=relation[i][j]
            key_list.add(temp)            
            if(len(key_list)==len_id and k not in find):
                find.append(k)
                answer+=1
            i+=1
        
            
    return answer

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])
