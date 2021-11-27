#그래프

def solution(n, results):
    answer = 0
    wins = {}
    loses = {}

    for a, b in results:
        wins[a]=[b]+wins[a]
        loses[b]=[a]+loses[a]
    
    for i in range(1, n+1):
        for loser in wins[i]: #i에게 진 사람들 list
            loses[loser] = loses[i]+loses[loser]
        for winner in loses[i]:
            wins[winner] = wins[i]+wins[winner]

    for i in range(1, n+1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            answer += 1

    return answer

solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
a={'b':[1,2,3]}
print(a['b'])