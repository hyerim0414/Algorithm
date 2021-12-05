#정렬

def solution(numbers):
    new_arr=[]
    result=""
    for num in numbers:
        new_arr.append(str(num))
    new_arr=sorted(new_arr)
    
    
    while(new_arr!=[]):
        split_same=[]
        N=new_arr[-1][0] #맨 앞 숫자
        
        split_same.append(new_arr.pop())
        while(new_arr!=[] and N==new_arr[-1][0]):
            split_same.append(new_arr.pop())
            continue
        
        i=0
        while(i<(len(split_same)-1)):
            j=i+1
            N=len(split_same[i])
            if(N==split_same[j+1]):
                while(j<len(split_same)-1) and N==len(split_same[j+1]):
                      j+=1
                split_same[i:j+1]=sorted(split_same,reverse=True)
            i=j+1
        for k in split_same:
            result+=k
    return result