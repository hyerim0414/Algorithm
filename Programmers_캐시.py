'''
- 큐를 이용해서 맨 앞에 있는거 제거
'''

from collections import deque
def solution(cacheSize, cities):
    answer = 0
    que=[]

    if(cacheSize==0): return 5*len(cities)
    for city in cities:
        city=city.lower()
        if(city in que):
            update=que.pop(que.index(city))
            que.append(update)
            answer+=1
            continue
        else:
            if(len(que)==cacheSize):
                que.pop(0)
            que.append(city)
            answer+=5

    return answer