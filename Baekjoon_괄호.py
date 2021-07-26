# 9012번

T=int(input())
for _ in range(T):
    command=input()
    check=1
    stack=[]
    for i in range(len(command)):
        if(command[i]=='('):
            stack.append(command[i])
        elif(stack!=[]):
            stack.pop()
        else:
            check=0
            break
    if(check==1 and stack==[]):
        print("YES")
    else:
        print("NO")
print()