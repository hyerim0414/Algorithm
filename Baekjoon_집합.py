import sys

S=[0 for _ in range(21)]

M=int(sys.stdin.readline())

for _ in range(M):
    s=sys.stdin.readline().strip()
    if(s=='all'):
        S=[1 for _ in range(21)]
    elif(s=='empty'):
        S=[0 for _ in range(21)]
    else:
        s,n=s.split()
        n=int(n)
        if(s=='add'):
            S[n]=1
        elif(s=='remove'):
            S[n]=0
        elif(s=='check'):
            print(S[n])
        elif(s=='toggle'):
            S[n]=0 if S[n] else 1
        
