#7568번

import sys 

N=int(sys.stdin.readline())
people=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
rank=[1 for _ in range(N)]

for i in range(N-1):
    for j in range(i,N):
        if(people[i][0]<people[j][0] and people[i][1]<people[j][1]):
            rank[i]+=1
        elif(people[j][0]<people[i][0] and people[j][1]<people[i][1]):
            rank[j]+=1

print(*rank)