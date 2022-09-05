from audioop import reverse


def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    inter = list(set(lost) & set(reserve))
    lost = [i for i in lost if i not in inter]
    reserve = [i for i in reserve if i not in inter]
    answer = n-len(lost)
    while n > answer and len(lost) != 0 and len(reserve) != 0:
        # print(n > answer)
        # print(len(lost))
        # print(len(reserve))
        if lost[0] == reserve[0]:
            lost.pop(0)
            reserve.pop(0)
            answer += 1
            continue
        if lost[0]+1 == reserve[0] or lost[0]-1 == reserve[0]:
            lost.pop(0)
            reserve.pop(0)
            answer += 1
            continue

        if lost[0] > reserve[0]:
            reserve.pop(0)
        else:
            lost.pop(0)
    
    return answer


print(solution(5, [1,2], [2,3]))


# 5	[2, 4]	[1, 3, 5]	5
# 5	[2, 4]	[3]	4
# 3	[3]	[1]	2