def solution(numbers, target):
    ans = dfs(numbers, target, 0)
    return ans

def dfs(n, t, d):
    ans = 0
    if len(n) == d:
        if sum(n) == t:
            return 1
        else:
            return 0
    else:
        ans += dfs(n, t, d + 1)
        n[d] *= -1
        ans += dfs(n, t, d + 1)
        return ans


print(solution([1, 1, 1, 1, 1], 3))
# [1, 1, 1, 1, 1]
# 3
# 5
# [4, 1, 2, 1]
# 4
# 2
