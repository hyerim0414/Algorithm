'''
- 아래->오른쪽->대각선 순으로 방향이 변경됨
- 각 방향마다 n번 -> n-1번 -> ... -> 1번 까지 움직임
- 3가지 방향이 rotation 
'''

def solution(n):
    answer = []
    table=[[0]*n for i in range(n)] #0으로 채워진 nxn 2차원 배열
    N=1
    p_x,p_y=-1,0 #이전 좌표
    for direction in range(n): 
        if(direction%3==0):
            p,q=1,0
        elif(direction%3==1):
            p,q=0,1
        else:
            p,q=-1,-1
        for go in range(n-direction):
            table[p_x+p][p_y+q]=N
            N+=1
            p_x, p_y = p_x+p, p_y+q
    #출력 형태로 변환
    for i in range(n):
        answer+=table[i][:i+1]
    return answer
