'''
- input() 함수 사용 시, 시간초과
- 시간단축을 위해 sys.stdin을 이용
- 입출력 속도 비교 : sys.stdin.readline > raw_input() > input()
'''
import sys
stack=[]

N=int(sys.stdin.readline())
for _ in range(N):
    command=sys.stdin.readline().split()
    if(command[0]=="push"):
        stack.append(int(command[1]))
    elif(command[0]=="pop"):
        print(stack.pop() if(stack!=[]) else -1)
    elif(command[0]=="size"):
        print(len(stack))
    elif(command[0]=="empty"):
        num=1 if(stack==[]) else 0
        print(num)
    elif(command[0]=="top"):
        print(stack[-1] if(stack!=[]) else -1)
print()