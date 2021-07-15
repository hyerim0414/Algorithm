def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    cam=routes[0][0]-1

    for route in routes:
        if(cam<route[0]):
            answer+=1
            cam=route[1]
            
    return answer