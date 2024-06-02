def solution(prices):
    stack = []
    ans = [i for i in range(len(prices)-1,-1,-1)]  
    
    for idx,p in enumerate(prices):
        #temp = 1
        while stack and p < prices[stack[-1]]:
            l=stack.pop()
            ans[l]=idx-l
            #temp += 1
        stack.append(idx)
    print(stack)
    return ans