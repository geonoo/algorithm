def solution(price, money, count):
    ans = money-(sum([price * i for i in range(1,count+1)]))
    return ans*-1 if ans < 0 else 0

print(solution(3, 20, 4))
# 3	20	4	10