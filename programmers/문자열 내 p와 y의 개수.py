def solution(s):
    cntP = 0
    cntY = 0
    for i in s:
        if i == 'p' or i == 'P':
            cntP += 1
        if i == 'y' or i == 'Y':
            cntY += 1

    return cntP == cntY

def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')

print(solution("pPoooyY"))