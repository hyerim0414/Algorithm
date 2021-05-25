'''
- 2x2 동일 문자 찾고 시작 인덱스를 리스트에 저장
- 리스트에서 하나씩 꺼내서 동일 문자를 '0'으로 변경하면서 카운트
- 열마다 중간에 '0' 이 있는 자리보다 위에 문자가 존재하면 위치 변경
(+ idea)
- 행렬을 오른쪽으로 90도 회전시키면, 중간 문자를 제거할 때마다 알아서 줄어드는 것을 이용하여 문제를 풀 수 있을 것 같다.
'''
def solution(m, n, board):
    answer = 0
    empty_col=[0]*n #열마다 정상 블록이 쌓여있는 행
    new_board=[]

    for i in range(m):
        new_board.append(list(board[i]))  #문자열, 문자로 나누기 위해 list로 casting
    board=new_board
    while(True):
        #겹치는 블록 찾아주기
        check=[]
        #print(empty_col[:-1])
        for j,row in enumerate(empty_col[:-1]): #열 별로 2x2 탐색       
            for i in range(m-2,row-1,-1):
                me, comp=board[i], board[i+1]
                if(me[j]==me[j+1] and me[j:j+2]==comp[j:j+2] and '0' not in me[j:j+2]+comp[j:j+2]):
                    check.append([i,j])
        if(check==[]):
            break
        #블록 없애기
        while(check!=[]):
            start_r,start_c=check.pop()
            #print(start_r,start_c)
            for p,q in [[0,0],[1,0],[0,1],[1,1]]: 
                if(board[start_r+p][start_c+q]!='0'):
                    board[start_r+p][start_c+q]='0'
                    empty_col[start_c+q]+=1
                    answer+=1
        #블록 없앤 부분 채워주기
        #print(board)
        for j in range(n):
            for i in range(m-1,0,-1):
                #print(i)
                if(board[i][j]=='0'):
                    change=i-1
                    
                    while(board[change][j]=='0' and change>0): #바꿀 수 있는 블록 찾기 (밑에서 위로)
                        change-=1
                    board[i][j], board[change][j]= board[change][j], board[i][j] 
                '''
                if(j==0):
                    for k in range(m):
                        print(board[k])
                    print()
                '''
        for k in range(m):
            print(board[k])
        print()
        
    return answer

a=solution(4,5,	["CCBDE", "AAADE", "AAABF", "CCBBF"])
print(a)