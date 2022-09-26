from collections import defaultdict


def solution(survey, choices):
    answer = ['Z','Z','Z','Z']
    score = defaultdict(int)
    score['A'] = 0
    score['C'] = 0
    score['F'] = 0
    score['J'] = 0
    score['M'] = 0
    score['N'] = 0
    score['R'] = 0
    score['T'] = 0
    for i in range(0, len(survey)):
        if choices[i] == 1:
            score[survey[i][0]] += 3
        elif choices[i] == 2:
            score[survey[i][0]] += 2
        elif choices[i] == 3:
            score[survey[i][0]] += 1
        elif choices[i] == 5:
            score[survey[i][1]] += 1
        elif choices[i] == 6:
            score[survey[i][1]] += 2
        elif choices[i] == 7:
            score[survey[i][1]] += 3
        
    
    for _ in range(0, len(score)):
        if score['R'] >= score['T']:
            answer[0] = 'R'
        else:
            answer[0] = 'T'

        if score['C'] >= score['F']:
            answer[1] = 'C'
        else:
            answer[1] = 'F'

        if score['J'] >= score['M']:
            answer[2] = 'J'
        else:
            answer[2] = 'M'

        if score['A'] >= score['N']:
            answer[3] = 'A'
        else:
            answer[3] = 'N'

    return ''.join(answer)



print(solution(["TR", "RT", "TR"], [7, 1, 3]))

# ["AN", "CF", "MJ", "RT", "NA"]	[5, 3, 2, 7, 5]	"TCMA"
# ["TR", "RT", "TR"]	[7, 1, 3]	"RCJA"

# 1번 지표	라이언형(R)	0	튜브형(T)	0
# 2번 지표	콘형(C)	0	프로도형(F)	0
# 3번 지표	제이지형(J)	0	무지형(M)	0
# 4번 지표	어피치형(A)	0	네오형(N)	0

# 3 2 1 x 1 2 3 
# 1 2 3 4 5 6 7