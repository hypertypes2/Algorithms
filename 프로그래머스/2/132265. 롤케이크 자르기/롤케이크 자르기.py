from collections import defaultdict

def solution(topping):
    cnt = 0
    left_dict = defaultdict(int)
    right_dict = defaultdict(int)
    
    for top in topping:
        right_dict[top]+=1

    for top in topping:
        left_dict[top]+=1
        right_dict[top]-=1
        if right_dict[top]==0:
            del right_dict[top]
        if len(left_dict)==len(right_dict):
            cnt+=1
        
    return cnt