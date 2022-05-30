
import sys
N, K = list(map(int, sys.stdin.readline().rstrip().split(' ')))
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline().rstrip()))

# print(N, K, lst)

start = 1
end = max(lst)

rtn = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for l in lst:
        if mid <= l:
            cnt = cnt + (l // mid)

    if cnt >= K:
        rtn = mid
        start = mid + 1
    else:
        end = mid - 1

print(rtn)


# 4 11
# 802
# 743
# 457
# 539