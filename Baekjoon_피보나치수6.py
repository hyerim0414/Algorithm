#11444번
'''
- 분할정복으로 피보나치 수 구하기 O(logN)
출처: https://janghw.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Divide-and-Conquer-%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5

-참고
https://shoark7.github.io/programming/algorithm/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%84-%ED%95%B4%EA%B2%B0%ED%95%98%EB%8A%94-5%EA%B0%80%EC%A7%80-%EB%B0%A9%EB%B2%95.html
10830번 행렬제곱
'''

import sys

#행렬곱
def multi(mat1,mat2):
    res=[]
    for i in range(2):
        res.append([])
        for j in range(2):
            temp=0
            for k in range(2):
                temp+=mat1[i][k]*mat2[k][j]
            res[i].append(temp%1000000007)
    return res


def power(mat, p):
    if(p==1):
        return mat
    else:
        temp=power(mat,p//2)
        if(p%2==0):
            return multi(temp,temp)
        else:
            return multi(multi(temp,temp),mat)


n=int(sys.stdin.readline())
base=[[1,1],[1,0]]
        
print(power(base,n)[0][1])