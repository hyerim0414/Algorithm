# 240916

import sys
from collections import deque

S, P = map(int,sys.stdin.readline().split())
dna_string = sys.stdin.readline().strip()
min_L = list(map(int, sys.stdin.readline().split()))

min_num = {'A':min_L[0],'C':min_L[1],'G':min_L[2],'T':min_L[3]}

cur_num = {'A':0,'C':0,'G':0,'T':0}

for i in range(P):
    cur_num[dna_string[i]]+=1

res=0
tmp=0
for dna in ['A','C','G','T']:
    if(cur_num[dna]<min_num[dna]):
        tmp=-1
        break

if(tmp==0):
    res +=1
for j in range(P,S):
    cur_dna = dna_string[j]
    post_dna = dna_string[j-P]

    cur_num[cur_dna]+=1
    cur_num[post_dna]-=1
    tmp=0
    for dna in ['A','C','G','T']:
        if(cur_num[dna]<min_num[dna]):
            tmp=-1
            break
    if(tmp==0):
        res +=1

print(res)

