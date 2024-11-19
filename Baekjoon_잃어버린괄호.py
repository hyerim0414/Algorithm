'''
24/11/19

- 최대 5자리 수 나올 수 있음
- 수는 0으로 시작할 수 있음
- 입력 길이 50보다 작거나 같

'''
import sys
s = sys.stdin.readline()[:-1]
oper = []
num = []

tmp = s.split("-")

res=sum(list(map(int,tmp[0].split("+"))))

for x in tmp[1:]:
    y = list(map(int,x.split("+")))
    res-=sum(y)

print(res)