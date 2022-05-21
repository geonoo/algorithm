def solution(answers):
    stu1 = [1, 2, 3, 4, 5]
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0]*3
    for i in range(len(answers)):
        if stu1[i % len(stu1)] == answers[i]:
            cnt[0] += 1
        if stu2[i % len(stu2)] == answers[i]:
            cnt[1] += 1
        if stu3[i % len(stu3)] == answers[i]:
            cnt[2] += 1

    # answer = []
    # for i in range(len(cnt)):
    #     if max(cnt) == cnt[i]:
    #         answer.append(i+1)

    return [i+1 for i in range(len(cnt)) if max(cnt) == cnt[i]]

print(solution([1,2,3,4,5]))