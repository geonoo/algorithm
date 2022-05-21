import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split(' '))
# print(N, M, V)
grahp = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
  i, j = map(int, sys.stdin.readline().split(' '))
  grahp[j][i] = grahp[i][j] = 1

# print(grahp)

def dfs(start,visited = []):
  visited.append(start)
  print(start, end=' ')

  for i in range(len(grahp[start])):
    if grahp[start][i] == 1 and i not in visited:
      dfs(i, visited)



def bfs(start):
  visited = [start]
  q = deque()
  q.append(start)
  while q:
    v = q.popleft()
    print(v, end=' ')

    for i in range(len(grahp[start])):
      if i not in visited and grahp[v][i] == 1:
        q.append(i)
        visited.append(i)

dfs(V)
print()
bfs(V)
