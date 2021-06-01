'''
- [[0]*(len(arr2[0]))]*(len(arr1)) 선언 시 얕은복사 (shallow copy)
- 얕은 복사는 단순히 요소를 복사하다 보니 바라보는 객체는 동일
- 이러한 방식으로 선언 뒤에, 값을 변경하게되면 다른 원소들도 값이 변경되는 현상이 발생 
'''

def solution(arr1, arr2):
    answer = [[0]*(len(arr2[0]))]*(len(arr1))
    for i in range(len(arr1)):
        for  j in range(len(arr2[0])):
            for k in range(len(arr2)):
                print(i,j)
                print(answer[i][j])
                answer[i][j]+=(arr1[i][k]*arr2[k][j])
    return answer