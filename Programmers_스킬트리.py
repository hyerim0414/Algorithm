'''
- skill에 대한 순서를 dictionary로 표현
- skill_tree에 dictionary에 있는 key를 발견했을 시, 현재 cur_skill 값과  dictionary 값 차가 -1이 아니면 false
'''

def solution(skill, skill_trees):
    answer = len(skill_trees)
    skill_book={}
    for i,char in enumerate(list(skill)):
        skill_book[char]=i; 
        
    for skill_tree in skill_trees:
        cur_skill=-1
        for stage in skill_tree:
            if(stage in skill_book.keys()):
                if(skill_book[stage]-cur_skill==1):
                    cur_skill=skill_book[stage]
                else:
                    answer-=1
                    break
    return answer