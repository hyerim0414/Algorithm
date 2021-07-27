#1874번

import sys
T=int(sys.stdin.readline())
num, max_i = 0, 0
stack=[]
seq=[]
check=True
for _ in range(T):
    i=int(sys.stdin.readline())
    if(max_i>i and seq[-1]<i ): 
        check=False
        break
    seq.append(i)
    max_i=i if(i>max_i) else max_i
if(check==False):
    print("NO")
else:
    for cur in seq:
        while(cur>num):
            print('+')
            num+=1
            stack.append(num)
        print('-') #무조건 한 번은 pop
        while(cur!=stack.pop()): 
            print('-')      
    print()