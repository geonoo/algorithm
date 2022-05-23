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
# print(combinationSum(candidates, target))

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    ans = []
    def dfs(arr, idx):
        s = sum(arr)
        if s > target:
            return
        if s == target:
            ans.append(arr)
            return
        for i in range(idx,len(candidates)):
            dfs(arr+[candidates[i]], i)
    dfs([], 0)
    return ans

candidates = [2, 3, 6, 7]
target = 7
print(combinationSum2(candidates, target))