#위클리 챌린지


def solution(price, money, count):
    temp=price*(count*(count+1))//2-money
    if(temp<0):
        return 0
    else:
        return temp