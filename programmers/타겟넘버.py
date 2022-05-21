import itertools


def solution(numbers, target):
    ans = dfs(numbers, target, 0)
    return ans

def dfs(n,t,d):
    ans = 0
    if len(n) == d:
        # print(n)
        if sum(n) == t:
            return 1
        else:
            return 0
    else:
        ans += dfs(n, t, d+1)
        n[d]*=-1
        ans += dfs(n,t,d+1)
        return ans

# print(solution([1,1,1,1,1], 3))

# [1, 1, 1, 1, 1]	3	5

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3




from itertools import product
def solution2(numbers, target):
    l = [(x, -x) for x in numbers]
    print(l)
    print(list(product(*l)))
    s = list(map(sum, product(*l)))
    return s.count(target)


# print(solution2([4,1,2,1], 4))

# def solution3(numbers, target):
#     ans = dfs(numbers, target, 0)
#     return ans
#
# def dfs(n, t, d):
#     ans = 0
#     if d == len(n):
#         if sum(n) == t:
#             return 1
#         else: return 0
#     else:
#         ans += dfs(n, t, d+1)
#         n[d] *= -1
#         ans += dfs(n, t, d+1)
#         return ans
#
# print(solution3([1, 1, 1, 1, 1], 3))

def solution4(numbers, target):
    ans = 0
    lst = [[x, -x] for x in numbers]
    return list(map(sum, itertools.product(*lst))).count(target)


print(solution4([1, 1, 1, 1, 1], 3))