def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i,p in enumerate(prices):
        while stack and p<prices[stack[-1]]:
            l=stack.pop()
            answer[l]=i-l           
        stack.append(i)
    if not stack:
        return answer
    for idx in stack:
        answer[idx]=len(prices)-1-idx
    return answer