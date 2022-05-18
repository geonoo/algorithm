def solution(n):

    sum = n
    for i in range(1,n//2+1,1):
        if n % i == 0:
            sum += i
    return sum

def solution2(num):
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

print(solution(12))
# 12	28
# 5	6