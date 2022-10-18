def solution(arr):
    temp = []
    answer = 0
    while len(arr) != 0:
        t = ''.join(sorted(str(arr.pop())))
        if t not in temp:
            answer += 1
            temp.append(t)
    return answer


print(solution([123, 456, 789, 321, 654, 987]))

