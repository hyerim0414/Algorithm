#2750번
'''
- 퀵정렬은 O(nlogn)
'''
import sys

def quick_sort(List):
    if(len(List)<=1):
        return List
    else:
        pivot=List[len(List)//2]
        left=[]
        equal=[]
        right=[]
        for n in List:
            if(n<pivot): left.append(n)
            elif(n>pivot): right.append(n)
            elif(n==pivot): equal.append(n)
        return quick_sort(left)+ quick_sort(equal) + quick_sort(right)  


T=int(sys.stdin.readline())

N=[]
for _ in range(T):
    N.append(int(sys.stdin.readline()))

sort_N=quick_sort(N)
for i in sort_N:
    print(i)
