from itertools import combinations_with_replacement
from collections import Counter


def solution(arrow, apeach):
    max_diff, max_comb_cnt = 0, {}

    for comb in combinations_with_replacement(range(11), arrow):
        cnt = Counter(comb)
        apeach_score, lion_score = 0, 0
        for i in range(11):
            if apeach[10 - i] < cnt[i]:
                lion_score += i
            elif apeach[10 - i] > 0:
                apeach_score += i

        diff = lion_score - apeach_score
        if diff > max_diff:
            max_diff = diff
            max_comb_cnt = cnt

    if max_diff == 0:
        return [-1]

    answer = [0]*11
    for k, v in max_comb_cnt.items():
        answer[10-k] = v


    return answer




arrow = 9
apeach = [0,0,1,2,0,1,1,1,1,1,1]
print(solution(arrow, apeach))

#lion = [0,2,2,0,1,0,0,0,0,0,0]

# 어쨋든 상대보다 많이 맞춰야 그 해당 점수를 가져가는 거다.

# 5	[2,1,1,1,0,0,0,0,0,0,0]	[0,2,2,0,1,0,0,0,0,0,0]
# 1	[1,0,0,0,0,0,0,0,0,0,0]	[-1]
# 9	[0,0,1,2,0,1,1,1,1,1,1]	[1,1,2,0,1,2,2,0,0,0,0]
# 10	[0,0,0,0,0,0,0,0,3,4,3]	[1,1,1,1,1,1,1,1,0,0,2]