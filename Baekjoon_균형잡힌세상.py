# 4949번
'''
- 정규표현식 사용
- [a-zA-Z] 알파벳 모두
'''

import re
pair={')':'(',']':'['}
while(True):
    command=input()
    if(command=='.'):
        break
    command=re.sub(r'[a-zA-Z]','',command.replace(' ',''))
    check=1
    stack=[]
    for i in range(len(command)-1):
        if(command[i] in ['(','[']):
            stack.append(command[i])
        elif(stack!=[]):
            if(pair[command[i]]!=stack.pop()):
                check=0
                break
        else:
            check=0
            break
    if(check==1 and stack==[]):
        print("yes")
    else:
        print("no")
print()