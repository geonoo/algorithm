import bisect
from typing import List


def search(nums: List[int], target: int) -> int:
    min_idx = sorted([[i,v] for i,v in enumerate(nums)], key=lambda x:x[1])[0][0]
    nums = nums[min_idx:] + nums[:min_idx]
    i = bisect.bisect_left(nums, target)
    print(i)
    if len(nums) > i and nums[i] == target:
        return (i+min_idx) % len(nums)
    else: return -1

print(search([5, 6, 0, 1, 2, 3, 4], 1))