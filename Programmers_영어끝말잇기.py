#Summer/Winter Coding(~2018)

'''
- 몇 번쨰에서 죽었는지 count 후, [count%n, count//n]
'''
def solution(n, words):
    answer = []
    past_words=[]
    end=words[0][0]
    count=1
    for word in words:
        if(word in past_words or end!=word[0]):
            break
        else:
            end=word[-1]
            past_words.append(word)
            count+=1
    if (count==len(words)+1):
        answer = [0,0]
    elif(count%n == 0 ):
        answer =[n,count//n ]
    else:
        answer = [count%n ,count//n +1]
    return answer