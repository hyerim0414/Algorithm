
import sys
N=int(sys.stdin.readline())


stone_game=[0 ] *1001
stone_game[1]=1
stone_game[3]=1
stone_game[2]=-1

for i in range(4,N+1):
    if ((stone_game[i-1]==1) and (stone_game[i-3]==1)):
        stone_game[i]=-1
    else:
        stone_game[i]=1

print("SK") if stone_game[N]==1 else print("CY")