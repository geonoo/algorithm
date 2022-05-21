from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    rtn = []
    def dfs(idx, arr=[]):
        rtn.append(arr)
        for i in range(idx, len(nums)):
            dfs(i+1, arr+[nums[i]])
    dfs(0)
    return rtn
print(subsets([1,2,3]))

# 입력: 숫자 = [1,2,3]
#  출력: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1, 2,3]]