import bisect
import itertools
from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    x, y = 0, len(numbers)-1
    while x < y:
        sum = numbers[x]+numbers[y]

        if sum < target:
            x += 1
        elif sum > target:
            y -= 1
        else:
            return [x + 1, y + 1]




# [0,0,3,4]
# 0
print(twoSum([-1000,-1,0,1],-1))

# Input: numbers = [2, 7, 11, 15], target = 9
# Output: [1, 2]