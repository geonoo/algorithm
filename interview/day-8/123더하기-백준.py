import sys

inputslen = int(sys.stdin.readline()[:-1])
inputs = [int(sys.stdin.readline()[:-1]) for _ in range(inputslen)]


def make_combi(n):
    def dfs(path):
        global answer
        sp = sum(path)
        if sp > n:
            return

        if sp == n:
            answer += 1
            return

        for i in range(1,4):
            dfs(path+[i])

    dfs([])
    print(answer)


for i in inputs:
    answer = 0
    make_combi(i)