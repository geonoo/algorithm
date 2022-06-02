import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(1, len(arr)):
    for j in range(len(arr[i])):
        if j == 0:
            arr[i][j] = arr[i-1][0]+arr[i][j]
        else:
            arr[i][j] = max(arr[i-1][j-1:j+1])+arr[i][j]

print(max(arr[-1]))