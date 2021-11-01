#탐욕법(Greedy)

def solution(n, costs):
    answer = 0
    check = [costs[0][0]]

    while(len(check)!=n):
        min_cost=0
        min_idx = 0
        min_des = 0
        for i,cost in enumerate(costs):
            if(cost[0] in check and cost[1] not in check):
                if(min_cost==0 or cost[2]<min_cost):
                    min_cost = cost[2]
                    min_idx = i
                    min_des = cost[1]
            elif(cost[1] in check and cost[0] not in check):
                if(min_cost==0 or cost[2]<min_cost):
                    min_cost = cost[2]
                    min_idx = i
                    min_des = cost[0]
        answer = answer + min_cost
        del costs[min_idx]
        check.append(min_des)

    return answer