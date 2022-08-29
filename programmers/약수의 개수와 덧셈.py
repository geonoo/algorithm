def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        div = getMyDivisor(i)
        if(div % 2 == 0):
            answer += i
        else:
            answer -= i

    return answer

def getMyDivisor(n):
    divisorsList = []
    for i in range(1, n + 1):
        if (n % i == 0) :
            divisorsList.append(i)
    return len(divisorsList)

print(solution(13,17))