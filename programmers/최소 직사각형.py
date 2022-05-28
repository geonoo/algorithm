def solution(sizes):
    answer = 0
    for s in sizes:
        if s[1] > s[0]:
            s[1], s[0] = s[0], s[1]
    max1 = 0
    max2 = 0
    for s in sizes:
        if max1 < s[0]:
            max1 = s[0]

    for s in sizes:
        if max2 < s[1]:
            max2 = s[1]

    return max1*max2


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
# [[60, 50], [30, 70], [60, 30], [80, 40]]	4000