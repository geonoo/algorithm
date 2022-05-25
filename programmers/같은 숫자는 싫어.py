def solution(arr):
    ans = []
    for i in arr:
        if len(ans) < 1:
            ans.append(i)
        else:
            if i != ans[-1]:
                ans.append(i)
    return ans

print(solution([1,1,3,3,0,1,1]))
# [1,1,3,3,0,1,1]	[1,3,0,1]