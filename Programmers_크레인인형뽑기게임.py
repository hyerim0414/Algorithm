#2019 카카오 개발자 겨울 인턴십
def solution(board, moves):
    answer = 0
    stack=[]
    for move in moves:
        for i in range(len(board)):
            if(board[i][move-1]==0):
                continue
            else:
                if(len(stack)>0 and stack[-1]==board[i][move-1]):
                    stack.pop()
                    answer+=2
                else:
                    stack.append(board[i][move-1])
                board[i][move-1]=0
                break
    return answer