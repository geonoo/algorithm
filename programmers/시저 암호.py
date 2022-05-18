def solution(s, n):
    answer = ''
    for i in s:
        c = ord(i)
        if 97 <= c and 123 >= c:
            print(c+n)
            if c+n > 122:
                answer += chr(c + n - 26)
            else:
                answer += chr(c + n)

        elif 65 <= c and 91 >= c:
            if c+n > 90:
                answer += chr(c + n - 26)
            else:
                answer += chr(c + n)
        else:
            answer += i

    return answer

print(solution("Z", 1))

# "AB"	1	"BC"