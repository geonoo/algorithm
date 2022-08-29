def solution(d, budget):
    answer = 0
    for v in sorted(d):
        budget = budget-v
        if(budget < 0):
            return answer
        answer+=1

    return answer

print(solution([2,2,3,3], 10))