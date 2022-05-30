import sys

N, M = list(map(int, sys.stdin.readline().rstrip().split(' ')))
lst = list(map(int, sys.stdin.readline().rstrip().split(' ')))

start = 1
end = max(lst)
rtn = 0

while start <= end:
    # 나무를 잘라야될 기준
    mid = (start + end) // 2
    cnt = 0
    for l in lst:
        if l > mid:
            # 기준값에서 빼서 내가 가져갈 나무의 길이
            cnt += l - mid

    # cnt : 우리가 가져갈 나무의 길이
    # M : 최소로 가져가야할 나무의 길이
    if cnt >= M:
        #start = 0
        #(3,4,5)
        start = mid + 1
    # 우리가 가져가야할 나무의 길이가 적다면
    # (0,1,2)
    else:
        end = mid - 1

print(end)

