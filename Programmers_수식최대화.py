#2020 카카오 인턴십

from itertools import permutations

def cal(priority, n, express):
    if n == 2:
        return str(eval(express))
    if priority[n] == '-':
        res = eval('-'.join([cal(priority, n+1, e) for e in express.split('-')]))
    elif priority[n] == '+':
        res = eval('+'.join([cal(priority, n+1, e) for e in express.split('+')]))
    else:
        res = eval('*'.join([cal(priority, n+1, e) for e in express.split('*')]))
    
    return str(res)

def solution(expression):
    answer=0
    for priority in permutations(['+','-','*']):
        answer = max(abs(int(cal(priority, 0, expression))), answer)
    return answer