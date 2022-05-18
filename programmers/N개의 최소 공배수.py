import math

def solution(arr):
    maxLcm = arr[0]
    for i in arr:
        maxLcm = lcm(maxLcm, i)
    return maxLcm


def lcm(x, y):
   return x * y // math.gcd(x,y)

# 유클리드 호제법
def gcd2(a, b):
    while b > 0:
        a, b = b, a % b
    return a



print(solution([2,6,8,14]))

# [2,6,8,14]	168
# [1,2,3]	6