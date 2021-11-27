def solution(answers):
    res=[]
    p1 = [1,2,3,4,5] 
    p2 = [2,1,2,3,2,4,2,5] 
    p3 = [3,3,1,1,2,2,4,4,5,5]
    
    p1_o,p2_o,p3_o=0,0,0

    for i in range(len(answers)):
        if(answers[i]==p1[i%5]):
            p1_o+=1
        if(answers[i]==p2[i%8]):
            p2_o+=1
        if(answers[i]==p3[i%10]):
            p3_o+=1
            
    answer = [p1_o, p2_o, p3_o]
    max_answer=max(answer)
    for i in range(3):
        if(answer[i]==max_answer):
            res.append(i+1)

    
    return res