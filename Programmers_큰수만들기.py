#탐욕법(Greedy)

def solution(number, k):
    answer = ''
    num=list(map(int,number)) 
    s=[num[0]]
    for i in range(1,len(num)):
        while(s!=[] and s[-1]<num[i] and k!=0) :
            s.pop()
            k-=1 
        s.append(num[i])    
    if k!=0:
        s=s[:-k]
    answer=''.join(map(str,s))
    return answer