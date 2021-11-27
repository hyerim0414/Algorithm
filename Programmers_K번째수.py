#정렬

def solution(array, commands):
    answer = []
    cut_arr=[]
    for command in commands:
        start,end,kth=command
        cut_arr=sorted(array[start-1:end])
        answer.append(cut_arr[kth-1])
    return answer