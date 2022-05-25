import heapq
from typing import List



def maxProduct(nums: List[int]) -> int:
    n = sorted(nums, reverse=True)
    return (n[0]-1)*(n[1]-1)

def maxProduct2(nums: List[int]) -> int:
    h = heapq.nlargest(2, nums)
    return (h[0] - 1) * (h[1] - 1)



print(maxProduct2([3,4,5,2,4,4,4,4,4]))