#깊이/너비 우선 탐색(DFS/BFS) 
  
from collections import deque

def solution(tickets):
    node={}
    q=deque(["ICN"])
    answer = []
    for s,e in tickets:
        if(s in node):
            node[s].append(e)
        else:
            node[s]=[e]
    
    for key in node.keys():
        node[key]=sorted(node[key],reverse=True)
    
    while(q):
        cur=q[-1]
        try:
            if(not node[cur]):
                answer.append(q.pop())
            else:
                q.append(node[cur].pop())
        except KeyError:
                node[cur] = []
    answer.reverse()
    return answer