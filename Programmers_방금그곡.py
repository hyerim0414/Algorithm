def solution(m, musicinfos):
    #한 문자로 인지하기 위해 코드 변경
    change={"C#":"H","D#":"I","F#":"J","G#":"K","A#":"L"} 
    for k in list(change.keys()):
        m=m.replace(k,change[k])
    candidate=[0,"(None)"]
    for music in musicinfos:
        start, end, title, code=music.split(",")
        time=(int(end[:2])-int(start[:2]))*60+(int(end[3:5])-int(start[3:5]))+1
        for k in list(change.keys()):
            code=code.replace(k,change[k])
        #음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생
        if(time!=len(code)): 
            code=code*(time//len(code))+code[:time%(len(code))]
        if(m in code and candidate[0]<time):
            candidate=[time,title]
    answer=candidate[1]
    return answer

