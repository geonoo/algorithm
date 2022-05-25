def solution(n):
    cnt = 0
    for i in range(2,n+1):
        if sosoo(i): cnt+=1
    return cnt

def sosoo(a):
    for i in range(2,int(a**(1/2))+1):
        if a % i == 0:
            return False
    return True




def solution2(n):
    num = set(range(2, n + 1))
    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
    
    return len(num)

print(solution2(100))