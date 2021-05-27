'''
- 짝수 -> 끝자리 1
- 홀수 -> 끝에서 0찾아서 1 그 전에꺼 0으로 변경
'''

def solution(numbers):
    answer = []
    for num in numbers:
        if(num%2==0):
            answer.append(num+1)
        else:
            temp=format(num,'b')
            i=temp.rfind('0')
            if(i==-1): temp='10'+temp[1:]
            else: temp=temp[:i]+'10'+temp[i+2:]
            answer.append(int(temp,2))    
    return answer