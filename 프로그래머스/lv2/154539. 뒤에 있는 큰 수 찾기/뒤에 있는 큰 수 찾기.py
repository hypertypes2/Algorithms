def solution(numbers):
    ans=[0]*len(numbers)
    stack=[]
    for i,n in enumerate(numbers):
        while stack and n>numbers[stack[-1]]:
            ans[stack.pop()]=n
        stack.append(i)
    for i in stack:
        ans[i]=-1
    return ans
