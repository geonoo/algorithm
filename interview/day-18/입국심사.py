def solution(n, times):
    times.sort()
    start = 1
    end = max(times)*n
    ans = 0
    while start <= end:
        mid = (start+end) // 2

        cnt = 0
        for t in times:
           cnt += mid // t

        if cnt >= n:
            ans = mid
            end = mid-1
        else:
            start = mid+1

    return ans

print(solution(6, [7, 10]))

# 6	[7, 10]	28