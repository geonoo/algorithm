import sys

N = int(sys.stdin.readline())
case = [int(sys.stdin.readline().strip()) for _ in range(N)]


# 1
# 2 -> 2
# 3 -> 4 (1,1,1,1), (1,2), (2,1), (3)
# 4 -> 7
def dfs(c):
    if c == 1 or c == 2:
        return c
    if c == 3:
        return 4
    if c == 4:
        return 7
    return dfs(c-3)+dfs(c-2)+dfs(c-1)

for c in case:
    print(dfs(c))