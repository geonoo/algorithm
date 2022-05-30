def solution(n, times):
    answer = 0
    start = 1
    end = max(times)*n
    while start <= end:
        mid = (start + end) // 2
        person = 0
        for t in times:
            person += mid // t

        if person >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1


    return answer

print(solution(6, [7, 10]))


# 6	[7, 10]	28