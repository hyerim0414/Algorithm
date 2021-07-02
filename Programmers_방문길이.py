'''
- path의 왼쪽 또는 아래의 점을 집합에 추가하여 방문했음을 표시
'''

def solution(dirs):
    go={"L":[-1,0],"R":[1,0],"U":[0,1],"D":[0,-1]}
    pos_x,pox_y=0,0
    LR_visited=set([])
    UD_visited=set([])
    for visit in dirs:
        move_x,move_y=pos_x+go[visit][0], pox_y+go[visit][1]
        # 미래의 점이 좌표평면 벗어나는지 확인
        if(move_x<-5 or move_x>5 or move_y <-5 or move_y>5):
            continue
        # 방문한 path의 왼쪽 또는 아래
        input=(min(pos_x,move_x),min(pox_y,move_y))
        
        if (visit in ["L","R"]):
            LR_visited.add(input)
        else:
            UD_visited.add(input)
        # 현 위치 업데이트
        pos_x,pox_y=move_x,move_y
    return len(list(LR_visited))+len(list(UD_visited))