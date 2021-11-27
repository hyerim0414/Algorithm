#탐욕법(Greedy)

def solution(people, limit):
    count = 0
    people.sort()
    i=0
    n=len(people)-1
    while(i<n):
        if(people[i]+people[n]<=limit):
            i+=1
        n-=1
        count+=1
    if(i==n):
        count+=1
            
    return count