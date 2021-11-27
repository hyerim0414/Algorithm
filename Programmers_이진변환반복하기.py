'''
- 진수 다루는 방법 : bin(int), format(int, 'b')
'''

def solution(s):
    answer = [0,0] #[이진변환횟수, 0갯수]
    while(len(s)!=1):
        print(s)
        answer[0]+=1
        answer[1]+=s.count('0')
        s=format(s.count('1'),'b') # 밑에 두 줄을 간소화 
        #s=s.replace('0','')
        #s=format(len(s),'b')     
    return answer