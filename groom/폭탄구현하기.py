import sys

n, k = map(int, sys.stdin.readline().strip().split())
matrix = [[0 for col in range(n)] for row in range(n)]
bomb = []
for _ in range(0,k):
    bomb.append(sys.stdin.readline().strip())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for idx in bomb:
    i = idx.split()
    x = int(i[0])-1
    y = int(i[1])-1
    matrix[x][y] += 1
    for j in range(0,4):
        if (x+dx[j]) >= 0 and (x+dx[j]) < n and (y+dy[j]) >= 0 and (y+dy[j]) < n:
            matrix[x+dx[j]][y+dy[j]] += 1

ans = 0
for m in matrix:
    ans += sum(m)

print(ans)