from functools import cmp_to_key
import sys

def solution(x, y):
    if x[0] == y[0]:
        if x[1] > y[1]:
            return 1
        else:
            return -1
    return 1

N, K = map(int, sys.stdin.readline().strip().split())

arr = []
for _ in range(0,N):
    arr.append(sys.stdin.readline().strip().split())

ans = sorted(arr, key=cmp_to_key(solution))

print(' '.join(ans[K-1]))
