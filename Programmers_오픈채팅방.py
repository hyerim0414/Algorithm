#2019 KAKAO BLIND RECRUITMENT

def solution(record):
    answer = []
    id_name={}
    for str in record:
        str_arr=str.split(" ")
        if (str_arr[0]=="Enter"):
            id_name[str_arr[1]]=str_arr[2]
        elif(str_arr[0]=="Change"):
            id_name[str_arr[1]]=str_arr[2]
            
    for str in record:
        str_arr=str.split(" ")
        if (str_arr[0]=="Enter"):
            answer.append(id_name[str_arr[1]]+"님이 들어왔습니다.")
        elif(str_arr[0]=="Leave"):
            answer.append(id_name[str_arr[1]]+"님이 나갔습니다.")
            
    return answer