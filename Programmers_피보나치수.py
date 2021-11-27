def solution(n):
    Fib=[0,1]
    for i in range(1,n):
        Fib.append(Fib[-1]+Fib[-2])
    return Fib[n]%1234567