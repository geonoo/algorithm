import sys

N, T = list(map(int, sys.stdin.readline().rstrip().split(' ')))
lst = list(map(int, sys.stdin.readline().rstrip().split(' ')))
print(N, T, lst)

start = 1
end = max(lst)

maxH = 0
while start < end:
    mid = (start + end) // 2
    h = 0
    for l in lst:
        if mid < l:
            h += l - mid

    print(h)
    if T <= h:
        maxH = mid
        start = mid + 1
    else:
        end = mid - 1

print(maxH)

# 4 6
# 18 19 10 17