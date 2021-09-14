#14888번
#삼성 SW 역량 테스트 기출 문제 1

import sys
from collections import deque
import copy

N=int(sys.stdin.readline())
origin_num=deque(list(map(int,sys.stdin.readline().split())))
origin_op=deque(list(map(int,sys.stdin.readline().split())))

max_res=-1000000000
min_res=1000000000


def back_tracking(num,op):
    global max_res,min_res
    if(len(num)==1):
        max_res=num[0] if(max_res<num[0]) else max_res
        min_res=num[0] if(min_res>num[0]) else min_res
    
    else:
        for i in range(4):
            ch_num=copy.deepcopy(num) 
            ch_op=copy.deepcopy(op)
            if(ch_op[i]!=0):
                ch_op[i]-=1
                a,b=ch_num.popleft(),ch_num.popleft()
                if(i==0):
                    ch_num.appendleft(a+b)
                elif(i==1):
                    ch_num.appendleft(a-b)
                elif(i==2):
                    ch_num.appendleft(a*b)
                else:
                    ck=1 if(a>=0) else -1
                    ch_num.appendleft(ck*(abs(a)//b))
                back_tracking(ch_num,ch_op)

back_tracking(origin_num,origin_op)
print(max_res)
print(min_res)