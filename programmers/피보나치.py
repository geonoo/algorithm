def solution(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
    return a%1234567

print(solution(4))

# F(2) = F(0) + F(1) = 0 + 1 = 1
# F(3) = F(1) + F(2) = 1 + 1 = 2
# F(4) = F(2) + F(3) = 1 + 2 = 3
# F(5) = F(3) + F(4) = 2 + 3 = 5


def solution2(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b, a+b
    return a

print(solution2(5))