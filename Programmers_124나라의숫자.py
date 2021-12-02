#연습문제
#124나라에서는 0은 4, 3으로 나눠서 나머지가 0일 시, 몫을 한 단계 줄이고 나머지를 4로 변경

base=[4,1,2]

def solution(n):
    num=''
    while(n>0):
        r=n%3
        n=n//3
        if(r==0):
            n-=1
        num=str(base[r])+num
    return num