#2018 KAKAO BLIND RECRUITMENT
'''
- 딕셔너리 이용
- 합집합은 max, 교집합은 min을 적절히 사용
'''

import re
import math

def solution(str1, str2):
    str1=str1.lower()
    str2=str2.lower()
    s1={}
    s2={}
    for i in range(len(str1)-1):
        s=str1[i:i+2]
        if(s.isalpha()):
            if(s in s1):
                s1[s]+=1  
            else:
                s1[s]=1
    for i in range(len(str2)-1):
        s=str2[i:i+2]
        if(s.isalpha() and len(s)==2):
            if(s in s2):
                s2[s]+=1  
            else:
                s2[s]=1
    inter={}
    uni=s1

    for i in s2:
        if(i in s1):
            inter[i]=min(s1[i],s2[i])
            uni[i]=max(s1[i],s2[i])
        else:
            uni[i]=s2[i]
            
    if(sum(uni.values())==0):
        return 65536

    return math.floor((sum(inter.values())) / sum(uni.values()) * 65536)