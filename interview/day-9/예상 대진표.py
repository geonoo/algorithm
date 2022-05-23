def solution(n,a,b):
    answer = 0
    t1 = [i for i in range(1,n+1)]
    t2 = []

    while t1 or t2:
        answer += 1
        if answer > 1 :
            t1,t2 = t2,[]
        for j in range(0, len(t1), 2):
            vs = t1[j:j+2]
            if a in vs and b in vs:
                return answer
            elif a in vs:
                t2.append(a)
            elif b in vs:
                t2.append(b)
            else:
                t2.append(vs[0])

    return answer

print(solution(8,4,7))


def solution2(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer

print(solution2(8,4,7))