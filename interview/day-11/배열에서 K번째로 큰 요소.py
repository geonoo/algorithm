import heapq
from typing import List



def findKthLargest(self, nums: List[int], k: int) -> int:
    return sorted(nums, reverse=True)[k-1]


def findKthLargest2(nums: List[int], k: int) -> int:

    return heapq.nlargest(k,nums)[-1]

print(findKthLargest2([3,2,1,5,6,4], 2))