def solution(n):
    lst = []
    for s in str(n):
        lst.append(int(s))
    lst.reverse()
    return lst

def digit_reverse(n):
    return list(map(int, reversed(str(n))))

print(solution(12345))
