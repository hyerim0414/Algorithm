#2020 KAKAO BLIND RECRUITMENT

def correct(s):
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


def solution(p):

    if(p==''):
        return ''
    current=p
    u=p
    v=''
    for i in range(2,len(current),2):
        if(current[:i].count('(')==current[:i].count(')')):
            u,v=current[:i],current[i:]
            break
    if(correct(u)==False):
        u=u[1:-1].replace("(",".").replace(")","(").replace(".",")")
        answer="("+solution(v)+")"+u
    else:
        answer=u+solution(v)
    return answer