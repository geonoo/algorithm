def solution(prices):
    answer = [0]*len(prices)
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1,len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                break
        answer[i] = cnt

    return answer

def solution2(prices):
    answer = [0]*len(prices)
    stack = []
    for i, v in enumerate(prices):
        while stack and prices[stack[-1]] > v:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    for i in stack:
        answer[i] = len(prices) - 1 - i

    return answer


print(solution2([1, 2, 3, 2, 3]))

#[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]