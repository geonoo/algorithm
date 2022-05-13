from typing import List


def reverseString(s: List[str]) -> List[str]:
    left, right = 0, len(s) -1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

def reverseString2(s : List[str]) -> List[str]:
    s.reverse()
    return s

print(reverseString2(['1','2','3','4','5']))