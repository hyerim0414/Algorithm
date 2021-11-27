def solution(n, t, m, p):
    answer = ''
    # n진법 사용되는 문자
    sample=list('0123456789ABCDEF')[:n] 
    allgame='0'
    # 1부터 t*m까지 숫자를 n진법으로 변환
    for i in range(1,(t*m+1)):
        temp=''
        while(i!=0):
            temp=sample[i%n]+temp
            i=i//n
        allgame+=temp
    # 내 차례 나오는 수
    for i in range(t):
        answer+=allgame[(p+m*i)-1]
    return answer