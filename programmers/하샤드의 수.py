def solution(x):
    return x % sum(list(map(int, str(x)))) == 0

print(solution(11))

# 10	true
# 12	true
# 11	false
# 13	false