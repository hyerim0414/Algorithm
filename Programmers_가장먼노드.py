from collections import deque
def solution(n, edge):
    answer = 0
    path = [0]*(n+1) #1까지의 거리
    edge=sorted(edge) 
    #print(edge)
    queue = deque() #다음 방문할 노드
    graph = [[] for i in range(n+1)] #graph[i]: i와 연결된 노드들 리스트
    
    for e in edge:  
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    queue.append(1)
    path[1] = 1
    
    while queue:
        node = queue.popleft()
        for g in graph[node]: #node와 연결된 노드 g , 1과 node의 path는 이미 찾음
            if path[g]==0:
                queue.append(g)
                path[g] = path[node]+1
        
    max_num= max(path)
    for n in path:
        if n == max_num:
            answer+=1               
    return answer