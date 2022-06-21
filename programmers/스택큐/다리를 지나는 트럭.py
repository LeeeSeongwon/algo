from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    inBridge = deque([0]*bridge_length)
    
    weight_sum = 0
    while truck_weights or sum(inBridge) > 0:
        answer += 1
        getOut = inBridge.popleft()
        weight_sum -= getOut
        
        if truck_weights and weight_sum + truck_weights[0] <= weight:
            getIn = truck_weights.popleft()
            weight_sum += getIn
            inBridge.append(getIn)
        else:
            inBridge.append(0)
    return answer

if __name__ == "__main__":
    assert solution(2, 10, [7, 4, 5, 6]) == 8