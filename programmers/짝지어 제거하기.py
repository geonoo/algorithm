from collections import OrderedDict


def solution(s):
    answer = 1
    while len(s) != 0:
        temp = []
        if temp[-1] == s[-1]:
            temp.pop()
            s.pop(0)
        temp.append(s.pop())
    print(temp)
    print(s)
    return answer

print(solution("cdcd"))

# baabaa	1
# cdcd	0