'''
- dictionary에 괄호 짝 미리 설정
- stack 이용
'''

def solution(s):
    code = {']':'[', '}':'{', ')':'('}
    front=['(','[','{']
    answer = 0
    rotation=0
    while(rotation <len(s)):
        check=True
        stack=[]
        for char in (s[rotation:]+s[:rotation]):
            if char in front:
                stack.append(char)
            elif (stack == [] or stack[-1]!=code[char]) :
                check=False
                break
            else:
                stack.pop()
        if(stack!=[]) : check=False
        
        if(check):
            answer+=1
            rotation+=2
        else:
            rotation+=1
    return answer
