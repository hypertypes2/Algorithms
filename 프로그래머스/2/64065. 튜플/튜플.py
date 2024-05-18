def solution(s):
    s = s[1:-1]
    temp = ''
    lst = []
    ans = []
    
    for char in s:
        if char == '{':
            array = []
        elif char.isdigit():
            temp += char
        elif char == ',' and len(temp)!=0:
            array.append(temp)
            temp = ''
        elif char=='}':
            array.append(temp)
            lst.append(array)
            temp = ''
    
    tuple = sorted(lst,key=lambda x:len(x))
    for tu in tuple:
        for t in tu:
            if int(t) not in ans:
                ans.append(int(t))
                
    return ans