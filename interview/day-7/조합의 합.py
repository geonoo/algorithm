import collections
import itertools
from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    rtn = []

    def dfs(csum, idx, arr):
        if csum == target:
            rtn.append(arr)
            return
        if csum > target:
            return
        for i in range(idx, len(candidates)):
            dfs(csum+candidates[i], i, arr+[candidates[i]])

    dfs(0, 0, [])
    return rtn

candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))

