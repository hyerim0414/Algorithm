#2019 카카오 개발자 겨울 인턴십

def solution(s):
    s=s[2:-2].split("},{")

    answer=[]
    set_ct={}

    for i in s:
        tmp=list(map(int,i.split(",")))
        for j in tmp:
            if(j in set_ct):
                set_ct[j]+=1
            else:
                set_ct[j]=1

    set_ct=sorted(set_ct.items(),key=lambda x: x[1],reverse=True)
    for i in set_ct:
        answer.append(i[0])
        
    return answer

s="{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))