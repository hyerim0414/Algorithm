#스택/큐

def solution(bridge_length, weight, truck_weights):
    time = 1
    num_waiting_truck=len(truck_weights)
    front=-1
    rear=0
    weight_sum=truck_weights[0]
    waiting_time_check=[bridge_length]
    while((front+1)!=num_waiting_truck):
        #다리 다 건넌 트럭 빼주기
        if(waiting_time_check[front+1]==1): #2생성->1생성 그 후 out 이므로 1에서 out            
            front+=1
            weight_sum-=truck_weights[front] #front옮기기 무게합빼주기
            
        # 다리 건너는 트럭 1초씩 움직임
        if((waiting_time_check!=[]) and (front!=rear)):
            for i in range(front+1,rear+1):
                waiting_time_check[i]-=1;
        #다리 오를 수 있는 트럭 넣어주기
        if((rear+1)<num_waiting_truck and (weight_sum+truck_weights[rear+1]<=weight)):
            rear+=1
            weight_sum+=truck_weights[rear]
            waiting_time_check.append(bridge_length)
        #print(waiting_time_check)
        time+=1
    answer=time
    return answer