def solution(n,a,b):
    answer = 0
    t1 = [i for i in range(1,n+1)]
    # 다음 대진을 담아둘 대진표
    t2 = []

    #t1, t2가 존재하는 동안 반복
    while t1 or t2:
        answer += 1
        #t1에다가 다음 대진표를 넣고, t2는 다시 그 다음 대진표를 넣을 준비
        if answer > 1 :
            t1,t2 = t2,[]
        #대진표의 배열 만큼 for문
        for j in range(0, len(t1), 2):
            # 2개씩 뽑아서 대결
            vs = t1[j:j+2]
            # 대진하는 사람이 A, B 이면 그동안 쌓았던 answer을 리턴
            if a in vs and b in vs:
                return answer
            # a가 승리해야하니까 a를 다음 대진에 참가
            elif a in vs:
                t2.append(a)
            # b가 승리해야하니까 a를 다음 대진에 참가
            elif b in vs:
                t2.append(b)
            # a,b 둘 다 없으면 그냥 홀수번째가 승리했다고 가정
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