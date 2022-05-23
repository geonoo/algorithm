import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split(' '))
lst = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split(' '))
    lst[i][j] = lst[j][i] = 1
print(lst)

def dfs(start, visited=[]):
    if start == 0:
        return
    visited.append(start)
    print(start, end=' ')

    for i, v in enumerate(lst[start]):
        if v == 1 and i not in visited:
            dfs(i)


def bfs(start):
    q = deque()
    q.append(start)
    visited = [start]
    while q:
        val = q.popleft()
        print(val, end=' ')
        for i in range(len(lst)):
            if lst[val][i] == 1 and i not in visited:
                q.append(i)
                visited.append(i)
dfs(v)
print()
bfs(v)