'''
- 01을 10으로 바꾸면 원래 숫자보다 큰 숫자 생성 가능
- 01뒤에 0과 1을 정렬시키면 큰 수 중 최소값 찾을 수 있음
'''

def solution(n):
    answer = 0
    s=format(n, 'b')
    idx=s.rfind("01")
    if(idx==-1):
        one=s[1:].count("1")
        s="10"+"0"*(len(s[1:])-one)+"1"*one
    else:
        one=s[idx+2:].count("1")
        s=s[:idx]+"10"+"0"*(len(s[idx+2:])-one)+"1"*one 
    print(s)
    answer=int(s,2)
    return answer