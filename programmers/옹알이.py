def solution(babbling):
    basic = ["aya", "ye", "woo", "ma"]
    s = babbling[0]
    i = 0
    while len(s) != 0 and i < 4:
        s = s.split(basic[i])[0]

    answer = 0
    return answer


print(solution(["aya", "yee", "u", "maa"]))

# ["aya", "yee", "u", "maa"]	1
# ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]	2