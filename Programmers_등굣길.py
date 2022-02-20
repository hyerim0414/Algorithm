#동적계획법(Dynamic Programming)
'''
- 왼->오, 위->아래
'''

def solution(m, n, puddles):
    puddle={}
    
    answer = 0
    walk=[[0]*(m+1) for _ in range(n+1)]
    
    for s,e in puddles:
        if(s in puddle):
            puddle[s].append(e)
        else:
            puddle[s]=[e]
    walk[1][1]=1
    #print(walk)
    for i in range(1,n+1):
        for j in range(1,m+1):
            if((i in puddle and j in puddle[i]) or i*j==1):
                continue
            else:
                walk[i][j]=walk[i][j-1]+walk[i-1][j]
    answer=walk[n][m]
    #print(walk)
    return answer

solution(4,3,[[2,2]])