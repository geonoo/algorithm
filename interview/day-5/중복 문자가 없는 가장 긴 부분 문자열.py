import collections


def lengthOfLongestSubstring(s: str) -> int:
    used = {}
    max_length = 0
    start = 0

    for i, v in enumerate(s):
        if v in used and start <= used[v]:
            start = used[v] + 1
        else:
            max_length = max(max_length, i - start + 1)
        used[v] = i

    return max_length



print(lengthOfLongestSubstring("tmmzuxt"))
#abcabcbb 3
#bbbbb 1
#pwwkew 3