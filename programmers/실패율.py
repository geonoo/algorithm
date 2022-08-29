def solution(N, stages):
    answer = []
    fail = {}
    participant = len(stages)
    for stage in range(1, N+1):
        # 분모가 0이 되면 안됌
        if participant != 0:
            cnt = stages.count(stage)
            fail[stage] = cnt / participant
            # 현재 레벨을 진행하는 사람은 다음 레벨을 진행할 수 없으므로 -cnt
            participant = participant - cnt
        else:
            fail[stage] = 0

    return sorted(fail, key=lambda x:fail[x], reverse=True)


#5 [2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
print(solution(5, [3,3,3,3]))
# 0.125
# 0.428571428571429
# 0.5
# 0.5
# 0