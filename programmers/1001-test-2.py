def solution(compressed):
    answer = compressed
    while "(" in answer:
        answer = solution2(answer)
    return answer

def solution2(compressed):
    num = []
    answer = ''
    b = []
    temp = ''
    for i in range(0, len(compressed)):
        if compressed[i].isdigit():
            if num and compressed[i-1].isdigit():
                num.append(num.pop()+compressed[i])
            else:
                num.append(compressed[i])
        elif compressed[i] == '(':
            if not compressed[i+1].isdigit():
                b.append(i)
        elif compressed[i] == ')' and b:
            bb = b.pop()
            answer = compressed.replace(compressed[bb-(len(num[-1])):i+1], (compressed[bb+1:i] * int(num.pop())))
        else:
            temp += compressed[i]
            
    return answer


print(solution("2(2(hi)2(co))x2(bo)"))

#"3(hi)" "hihihi"
#"2(3(hi)co)" "hihihicohihihico"
#"10(p)" "pppppppppp"
#"2(2(hi)2(co))x2(bo)" "hihicocohihicocoxbobo"