from collections import defaultdict
table = {')':'('} 

def isright(s):
    stack = []
    for char in s:
        if not stack or char not in table:
            stack.append(char)
            continue
        if table[char] == stack[-1]:
            stack.pop()
    
    return False if stack else True 
    
def solution(p):
    ans = ''
    
    dict = defaultdict(int)
    if isright(p):
        return p
    for i in range(len(p)):
        dict[p[i]]+=1
        if dict['(']==dict[')']:
            break
            
    u,v = p[:i+1],p[i+1:]

    if isright(u):
        ans += u+solution(v)
    else:
        temp = '('+ solution(v) +')'
        for c in u[1:-1]:
            if c=='(':
                temp += ')'
                continue
            temp += '('
        ans += temp
    return ans