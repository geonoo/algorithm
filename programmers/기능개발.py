import collections
import math


def solution(progresses, speeds):
    answer = []
    day = []
    #날짜를 계산해서 day리스트에 담기
    for i in range(len(progresses)):
        d = math.ceil((100 - progresses[i]) / speeds[i])
        day.append(d)

    cnt = 1
    #day의 길이 - 1 만큼 돌리기
    for i in range(len(day)-1):
        #앞에 날짜가 뒤에 날짜보다 작으면
        if day[i] < day[i + 1]:
            #혼자 빠져야함
            answer.append(cnt)
            cnt = 1
        # 앞에 날짜가 뒤에 날짜보다 크거나 같으면
        else:
            #뒤에 날짜를 앞에 날짜로 바꾸고 ( 그래야 기준값이 오니까 ) 카운트 + 1
            day[i + 1] = day[i]
            cnt += 1

    #마지막 으로 계산한 날짜를 넣어줘야함.
    answer.append(cnt)
    return answer


print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))


# [93, 30, 55]	[1, 30, 5]	[2, 1]
# [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]