'''
- union & find 이용
'''

def solution(n, computers):
    answer = 0
    parent = [i for i in range(n)]
    def find(target):
        if target == parent[target]:
            return target
        parent[target] = find(parent[target])
        return parent[target]
    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
        
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 0:
                continue
            else:
                union(i, j)

    for i in range(n):
        parent[i] = find(i)
    answer = len(set(parent))
    return answer