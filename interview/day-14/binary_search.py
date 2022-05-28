def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1

print(binary_search([1,2,3,4,5,6,7,8,9],8,0,8))

# while start <= end:
#     mid = (start + end) // 2
#     # 찾은 경우 반환
#     if arr[mid] == target:
#         return mid
#
#     # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
#     elif arr[mid] > target:
#         end = mid - 1
#     # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽확인
#     else:
#         start = mid + 1
# return None
