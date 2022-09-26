def solution(s):
    cnt, zero = 0,0

    while(s != "1"):
        zero += s.count("0")
        s = format(len(s.replace('0','')), 'b')
        cnt += 1
        print(s)

    answer = [cnt,zero]

    return answer

print(solution("1111111"))

# "110010101001"	[3,8]
# "01110"	[3,3]
# "1111111"	[4,1]