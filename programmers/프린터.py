from collections import deque


def solution(priorities, location):
    # doc -> ABCD를 0123 이라고 하고 이것을 인덱스로 사용
    doc, cnt = deque(range(len(priorities))), 0
    while doc:
        if priorities[doc[0]] == max(priorities):
            if doc[0] == location:
                cnt +=1
                break
            else:
                cnt += 1
                priorities[doc[0]] = -1
                doc.popleft()
        else:
            doc.append(doc.popleft())

    return cnt

print(solution([1, 1, 9, 1, 1, 1], 0))

# [2, 1, 3, 2]	2	1
# [1, 1, 9, 1, 1, 1]	0	5