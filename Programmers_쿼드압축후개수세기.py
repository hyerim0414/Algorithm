def solution(arr):
    answer = [0,0]
    def quadtree(x,y,size):
        match=arr[x][y]
        for i in range(x,x+size):
            for j in range(y,y+size):
                if(match!=arr[i][j]):
                    size=size//2
                    quadtree(x,y,size)
                    quadtree(x,y+size,size)
                    quadtree(x+size,y,size)
                    quadtree(x+size,y+size,size)
                    return
        answer[match]+=1
    quadtree(0,0,len(arr))
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))