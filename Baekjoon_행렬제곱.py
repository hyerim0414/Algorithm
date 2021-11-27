#10830번

import sys

def multi(mat1,mat2):
    C = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]

    for n in range(len(mat1)):
        for k in range(len(mat2[0])):
            for m in range(len(mat2)):
                C[n][k] += mat1[n][m] * mat2[m][k]
            C[n][k]=C[n][k]%1000

    return C

def power(mat, p):
    if(p==1): 
        return mat
    else:
        temp=power(mat,p//2)
        if(p%2==0): 
            return multi(temp,temp)
        else:
            return multi(mat,multi(temp,temp))


n,p=map(int,sys.stdin.readline().split())
A = [list(map(int,input().split())) for i in range(n)]

for i in power(A,p):
    for j in i:
        print(j%1000, end = ' ') #matrix size가 1일때 고려사항
    print()