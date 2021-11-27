'''
- stack 사용
'''

def solution(s):
    answer = True
    stack=[]
    for char in s:
        if char == "(":
            stack.append(char)
        elif stack == [] :
            return False
        else:
            stack.pop()
    return stack ==[] #비어있으면 모두 짝 완성, 비어있지 않으면 완성되지 않은 괄호 존재
