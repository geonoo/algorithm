import sys

N = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split(' ')))

print(N, lst)

# 5
# -15 -6 1 3 7
lo = 0
hi = N

while lo < hi:
    mid = (lo + hi) // 2
    if lst[mid] < mid:
        lo = mid+1
    else:
        hi = mid

if lo >= len(lst) or lo != lst[lo]:
    print(-1)
else:
    print(lo)