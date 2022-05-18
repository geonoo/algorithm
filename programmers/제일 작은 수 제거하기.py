def solution(arr):
    arr.remove(min(arr))
    return [-1] if not arr else arr

print(solution([4,3,2,1]))