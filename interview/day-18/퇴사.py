import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

print(arr)


max_val = 0
def dp(idx, pay):
    global max_val
    if idx >= N:
        if pay > max_val:
            max_val = pay
        return

    t, p = arr[idx]

    for i in range(2):
        if i == 1:
            if idx + t > N:
                return
            dp(idx + t, pay + p)
        else:
            dp(idx + 1, pay)
dp(0, 0)
print(max_val)