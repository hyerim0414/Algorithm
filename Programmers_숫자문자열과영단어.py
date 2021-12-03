#2021 카카오 채용연계형 인턴십

def solution(s):
    N='0123456789'
    num=['zero','one','two','three','four','five','six','seven','eight','nine']

    cur=0
    answer = ''

    while(cur<len(s)):
        if(s[cur] in N):
            answer+=s[cur]
            cur+=1
        else:
            for i in range(10):
                l=len(num[i])
                if(s[cur:cur+l]==num[i]):
                    cur+=l
                    answer+=str(i)
                    break
    
    return int(answer)