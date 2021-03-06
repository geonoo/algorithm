import string


def get_idx_naive(word):
    result = [-1]*len(string.ascii_lowercase)
    for i in range(len(word)):
        char = word[i]
        for j in range(len(string.ascii_lowercase)):
            lo = string.ascii_lowercase[j]
            if result[j] == -1 and char == lo:
                result[j] = i
    print(' '.join([str(num) for num in result]))


def get_idx(word):
    # point 1. ord
    # point 2. O(n^2) -> O(n)
    result = [-1]*len(string.ascii_lowercase)
    for i in range(len(word)):
        idx = ord(word[i]) - 97
        if result[idx] == -1:
            result[idx] = i
    print(' '.join([str(num) for num in result]))


S = input()
check = [-1] * 26

for i in range(len(S)):
    if check[ord(S[i]) - 97] == -1:
        check[ord(S[i]) - 97] = i

for i in range(26):
    print(check[i], end=' ')

#get_idx_naive('baekjoon')
# get_idx('baekjoon')