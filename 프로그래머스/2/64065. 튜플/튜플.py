def solution(s):
    s = s[1:-1]
    temp = ''
    lst = []
    ans = []
    
    for char in s:
        if char == '{':
            temp = ''
        elif char == '}':
            lst.append(list(map(int,temp.split(','))))
        else:
            temp += char
    
    tuple = sorted(lst,key=lambda x:len(x))
    for tu in tuple:
        for t in tu:
            if int(t) not in ans:
                ans.append(int(t))
                
    return ans