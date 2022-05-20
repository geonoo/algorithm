import sys

n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().strip())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

dangi = 0
dangiCnt = []
for i in range(n):
    for j in range(n):
        if lst[i][j] == 0:
            continue

        cnt = 0
        dangi +=1
        stack = [[i, j]]
        while stack:
            y, x = stack.pop()
            if lst[y][x] != 0:
                lst[y][x] = 0
                cnt += 1

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= n or lst[ny][nx] == 0:
                    continue
                stack.append([ny, nx])

        dangiCnt.append(cnt)

print(dangi)
for i in sorted(dangiCnt):
    print(i)






# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

# 3
# 7
# 8
# 9