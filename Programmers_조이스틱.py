#탐욕법(Greedy)

def solution(name):
    answer = 0
    a, z =ord('A'),ord('Z')
    new_name=[min(ord(x)-a,z+1-ord(x)) for x in name]
    answer+=sum(new_name)
    
    i=0
    while(1):
        left,right=1,1
        new_name[i]=0
        if sum(new_name)==0 : 
            break
        
        left, right = 1,1
        for l in range(1,len(new_name)):
            if new_name[i-l] == 0: left += 1
            else: break
        
        for r in range(1,len(new_name)):
            if new_name[i+r] == 0: right += 1
            else: break
        
        answer+=left if(left<right) else right
        i += -left if(left<right) else right
    
            
    return answer