import math


def solution(n):
    s = (math.sqrt(n)+1)**2
    return -1 if s % 1 != 0 else s

print(solution(121))