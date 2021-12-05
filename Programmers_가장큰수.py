#정렬

'''
- 1,000 이하의 숫자들 비교를 위해 *3을 해줌
- 0만 들어왔을 때, 0을 출력하기 위해 예외사항 추가
'''

def solution(numbers):
    result=''
    if(sorted(numbers)[-1]==0):
        return '0'
    else:
        
        new_arr=[[str(x),str(x)*3] for x in numbers]
        new_arr=sorted(new_arr,key=lambda x: x[1], reverse=True)
        for i in new_arr:
            result+=i[0]
        return result