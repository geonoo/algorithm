import itertools
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    rtn = [[]]
    for i in nums:
        rtn.append([i])
    for i in range(2, len(nums)+1):
        for j in list(itertools.combinations(nums, i)):
            rtn.append(j)

    return rtn

def subsets2(nums: List[int]) -> List[List[int]]:
    rtn = []
    def dfs(idx, arr):
        rtn.append(arr)

        for i in range(idx, len(nums)):
            dfs(i+1, arr+[nums[i]])


    dfs(0, [])
    return rtn




print(subsets2([1,2,3]))