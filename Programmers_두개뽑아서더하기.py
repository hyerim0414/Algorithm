#월간 코드 챌린지 시즌1

from itertools import combinations
def solution(numbers):
    answer = set()
    for i in list(combinations(numbers,2)):
        answer.add(sum(i))
    return sorted(answer)