import sys

N = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split(' ')))

print(N, lst)


def install_router(lst, C):
    # 1. 이분탐색을 위한 정렬
    lst.sort()

    start = 1
    end = lst[-1] - lst[0]
    min = 0
    while start <= end:
        mid = (start + end ) // 2
        cnt = 1
        cur = lst[0]
        for i in range(1, len(lst)):
            if lst[i] >= mid + cur:
                cnt +=1
                cur = lst[i]

        if cnt >= C:
            start = mid + 1
            min = mid
        else:
            end = mid - 1

    return min

print(install_router([1, 2, 8, 4, 9], 3))
# assert install_router([1, 2, 8, 4, 9], 3) == 3
