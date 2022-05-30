import sys

N = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split(' ')))
yesan = int(sys.stdin.readline().rstrip())

# print(N, lst, yesan)

start = 0
end = max(lst)
while start <= end:
    mid = (start + end) // 2
    total = 0
    for l in lst:
        if mid >= l:
            total += l
        else:
            total += mid

    if total <= yesan:
        start = mid + 1
    else:
        end = mid - 1

print(end)

# 4
# 120 110 140 150
# 485