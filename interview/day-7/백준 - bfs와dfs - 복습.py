import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split(' '))
lst = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split(' '))
    lst[i][j] = lst[j][i] = 1
print(lst)

def dfs(start, visited=[]):
    print(start, end=' ')
    visited.append(start)
    for i in range(len(lst[start])):
        if lst[start][i] == 1 and i not in visited:
            dfs(i)



def bfs(start):
    q = deque()
    q.append(start)
    visited = [start]
    while q:
        k = q.popleft()
        print(k, end=' ')
        for i in range(len(lst[start])):
            if i not in visited and lst[k][i] == 1:
                q.append(i)
                visited.append(i)

dfs(v)
print()
bfs(v)