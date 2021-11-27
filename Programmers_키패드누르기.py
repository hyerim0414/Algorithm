def solution(numbers, hand):
    L_pos=[4,1]
    R_pos=[4,3]
    answer = ''
    for num in numbers:
        if(num in [1,4,7]):
            answer+='L'
            L_pos=[num//3+1,1]
        elif(num in [3,6,9]):
            answer+='R'
            R_pos=[num//3,3]
        else:
            if(num==0):
                num_pos=[4,2]
            else:
                num_pos=[num//3+1,2]
            L=sum(abs(i-j) for i,j in zip(num_pos,L_pos))
            R=sum(abs(i-j) for i,j in zip(num_pos,R_pos))
            if(L<R):
                answer+='L'
                L_pos=num_pos
            elif(R<L):
                answer+='R'
                R_pos=num_pos
            else:
                answer+='R' if(hand=='right') else 'L'
                if(hand=='right'):
                    R_pos=num_pos
                else:
                    L_pos=num_pos
            
    return answer