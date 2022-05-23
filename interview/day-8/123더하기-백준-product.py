import itertools
import sys

N = int(sys.stdin.readline())
case = [int(sys.stdin.readline().strip()) for _ in range(N)]

for c in case:
    cnt = 0
    for j in range(1, c+1):
        cnt += [sum(i) for i in list(itertools.product([1,2,3], repeat=j))].count(c)

    print(cnt)