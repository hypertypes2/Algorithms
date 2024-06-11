def solution(record):
    ans = []
    dict = {}
    
    for char in record:
        X = char.split(' ')
        if len(X) == 3:
            dict[X[1]] = X[2]
            
    for char in record:
        X = char.split(' ')
        if X[0] == 'Enter':
            ans.append(dict[X[1]] + "님이 들어왔습니다.")
        elif X[0] == 'Leave':
            ans.append(dict[X[1]] + "님이 나갔습니다.")
        else:
            continue
    
    return ans