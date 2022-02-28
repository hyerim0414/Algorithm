#2022 KAKAO BLIND RECRUITMENT

def solution(fees, records):
    answer = []
    time={} #차번호:주차시간
    rec={}
    for i in records:
        a,b,c=i.split()
        if(c=='IN'):
            rec[b]=a
        elif(c=='OUT'):
            start=rec[b]
            end=a
            del rec[b]
            tot=60*(int(end[:2])-int(start[:2]))+int(end[3:])-int(start[3:])
            if(b in time):
                time[b]+=tot
            else:
                time[b]=tot
    if(rec):
        for i in rec.keys():
            tot=60*(23-int(rec[i][:2]))+59-int(rec[i][3:])
            if(i in time):
                time[i]+=tot
            else:
                time[i]=tot
    time=sorted(list(time.items()))
    for i,j in time:
        price=fees[1]
        if(j-fees[0]>0):
            price+=((j-fees[0]-1)//fees[2]+1)*fees[3]
        answer.append(price)
    
    return answer