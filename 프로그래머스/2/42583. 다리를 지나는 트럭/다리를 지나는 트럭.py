def solution(bridge_length, weight, truck_weights):
    stack = truck_weights[::-1]
    bridge = []
    time = 0

    while stack or bridge:
        time +=1
        for x,y in bridge:
            if x >= bridge_length:
                bridge.pop(0)
                
        if not stack and not bridge:
            break
            
        if stack:
            sum = 0
            for b in bridge:
                sum += b[1]
            now = stack[-1]
            if len(bridge)+1 <= bridge_length and sum+now <= weight:
                bridge.append([0,stack.pop()])

        for i in range(len(bridge)):
            bridge[i][0] += 1 

    return time     