def logestPalindrome(s: str) -> str:
    def expand(left: int, right: int) -> str:
        # 팰린드롬 여부를 체크하며 포인터 확장
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        return s[left + 1:right - 1]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''

    for i in range(len(s) - 1):
        # 팰린드롬은 짝수, 홀수 경우 모두 나타나기 때문에 2가지 형태의 포인터 사용
        result = max(result,expand(i, i + 1),expand(i, i + 2),key=len)

    return result


#print(logestPalindrome('babad'))


def logestPalindrome(s):
    list = []
    for idx1, val1 in enumerate(s):
        for idx2, val2 in enumerate(s[::-1]):
            if val1 == val2 and idx1 != len(s)-1-idx2:
                # print(idx1, val1)
                # print(len(s)-1-idx2, val2)
                # print(s[min(idx1,len(s)-1-idx2):max(idx1,len(s)-1-idx2)+1])
                list.append(s[min(idx1,len(s)-1-idx2):max(idx1,len(s)-1-idx2)+1])
    return max(set(list), key=len)


print(logestPalindrome('babad'))