def solution(s):
    answer = ''
    lst = s.split(' ')
    for i in range(len(lst)):
        temp = ''
        for j, v in enumerate(lst[i]):
            if j % 2 == 0:
                temp += v.upper()
            else:
                temp += v.lower()
        answer += temp+' '


    return answer[:-1]

#	"TrY HeLlO WoRlD"

print(solution("try hello world"))