def solution(phone_book):
    answer = True
    temp=-1
    phone_book.sort()
    for idx,p_num in enumerate(phone_book[:-1]):
        if phone_book[idx+1].startswith(p_num): 
            answer=False
            break
    return answer