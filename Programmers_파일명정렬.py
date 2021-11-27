def solution(files):
    num='0123456789'
    new_files=[]
    for file in files:
        i=0
        while(i < len(files)):
            if(file[i] not in num):
                i+=1
            else:
                break
        for j in range(i+1,i+6):          
            if(j>=len(file) or file[j] not in num):
                break

        head,number=file[:i].lower(),file[i:j].zfill(5)
        new_files.append([head,number,file])

    new_files=sorted(new_files,key = lambda x : (x[0], x[1]))
    answer=[ new_files[i][2] for i in range(len(files))]
    return answer
