import sys
from itertools import combinations

N=int(sys.stdin.readline().strip())

student_count={i:0 for i in range(N)}
students_list=[]
for i in range(N):
    student = list(map(int,sys.stdin.readline().strip().split()))
    students_list.append(set([(a,b) for a,b in enumerate(student)]))

combi_list=combinations(range(N),2)

for combi in combi_list:
    res=students_list[combi[0]] & students_list[combi[1]]
    if(len(res)>0):
        student_count[combi[0]]+=1
        student_count[combi[1]]+=1


res=sorted(student_count.items(),key= lambda x: -x[1])

print(res[0][0]+1) #python index start 0
