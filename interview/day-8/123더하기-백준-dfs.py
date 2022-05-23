import sys

N = int(sys.stdin.readline())
case = [int(sys.stdin.readline().strip()) for _ in range(N)]

def dfs(n, arr):
    global ans
    s = sum(arr)
    if s > n:
        return
    if s == n:
        ans += 1
        return
    for i in range(1, 4):
        dfs(n, arr+[i])


for c in case:
    ans = 0
    dfs(c, [])
    print(ans)