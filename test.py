
def abc(word):
    c = [-1]*26
    for i in range(len(word)):
        idx = ord(word[i]) - 97
        if c[idx] == -1:
            c[idx] = i
    print(' '.join([str(num) for num in c]))


abc('baekjoon')

