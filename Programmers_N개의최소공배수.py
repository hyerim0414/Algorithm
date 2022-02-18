#연습문제

from math import gcd

def solution(arr):
    g=arr[0]
    l=arr[0]
    for i in range(1,len(arr)):
        g=gcd(l,arr[i])
        l=(l*arr[i])//g

    return l