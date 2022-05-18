import math

def solution(n, m):
    answer = []
    answer.append(math.gcd(n, m))
    answer.append(n*m // math.gcd(n, m))
    return answer

def solution2(n, m):
    return [math.gcd(n, m), n*m // math.gcd(n, m)]

print(solution2(3, 12))


