
import sys

while(True):
    x=list(map(int,sys.stdin.readline().split()))
    a,b,c=sorted(x)
    if(a==0):
        break
    if(b-a>=c or a+b<=c):
        print('Invalid')
    else:
        if(a!=b and b!=c):
            print("Scalene")
        elif(a!=c):
            print("Isosceles")
        else:
            print("Equilateral")

