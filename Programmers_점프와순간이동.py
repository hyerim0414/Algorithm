#Summer/Winter Coding(~2018)

def solution(n):
    ans = 0
    while(n!=0):       
        ans+= 1 if(n%2==1) else 0
        n=n//2

    return ans