import sys

s=(sys.stdin.readline()).lower()
alphabet={}

for i in s[:-1]:
    if(alphabet.get(i)==None):
        alphabet[i]=1
    else:
        alphabet[i]+=1


res=sorted(alphabet.items(),key= lambda x: -x[1])

if((len(res)>1) and (res[0][1]==res[1][1])): #input이 2개 이상일때만 비교가능
    print("?")
else:
    print(res[0][0].upper())

