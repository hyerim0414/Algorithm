#2020 KAKAO BLIND RECRUITMENT

def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        split_str=""
        j=0
        num=1
    
        for j in range(0,len(s),i):
            if(s[j:j+i]==s[j+i:j+2*i]):
                num+=1
                remember=s[j:j+i]
                continue
            else:
                if(num!=1):
                    split_str+=(str(num)+remember)
                else:
                    split_str+=s[j:j+i]
                num=1

        answer= len(split_str) if(len(split_str)<answer) else answer
        
    return answer