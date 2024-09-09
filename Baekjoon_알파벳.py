import sys

R,C = list(map(int,sys.stdin.readline().strip().split()))
board=[]
moving=[(0,1),(1,0),(0,-1),(-1,0)]

max_count=0

for _ in range(R):
    c = sys.stdin.readline().strip()
    board.append(c)

visited=set([board[0][0]])

def move(node,count):
    global max_count #얘가 핵심임...
    max_count = max(max_count,count)
    x,y=node
    for m_x,m_y in moving:
        next_x, next_y = x+m_x, y+m_y
        if((0>next_x) or (0>next_y) or (next_y>C-1) or (next_x>R-1)):
            continue

        if(board[next_x][next_y] not in visited): # 여기서도 계속 원소 있는지 체크 시간 소모
            visited.add(board[next_x][next_y])
            move((next_x,next_y),count+1)
            visited.remove(board[next_x][next_y])

    
move((0,0),1)
print(max_count)
    




