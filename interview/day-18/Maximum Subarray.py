from typing import List


def maxSubArray(nums: List[int]) -> int:

    m = nums[0]
    point = 0
    l = len(nums)
    start = 0
    end = len(nums)
    while point < l:
        print(nums[point: l])
        m = max(m, sum(nums[point: l]))
        m = max(m, sum(nums[0: l-point]))
        m = max(m, sum(nums[point: l-point]))
        point+=1

    return m


# [1,2,-1,-2,2,1,-2,1,4,-5,4]
# [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6