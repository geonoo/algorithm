def solution(arr, divisor):
    answer = []
    for i in sorted(arr):
        if i % divisor == 0:
            answer.append(i)
    return [-1] if not answer else answer


print(solution([5, 9, 7, 10],5))
# [5, 9, 7, 10]	5	[5, 10]
# [2, 36, 1, 3]	1	[1, 2, 3, 36]
# [3,2,6]	10	[-1]