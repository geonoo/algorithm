import itertools
from functools import cmp_to_key
from typing import List


def largestNumber(nums: List[int]) -> str:
    nums = [str(i) for i in nums]

    def comparator(i, j):
        if int(i + j) > int(j + i):
            return -1
        else:
            return 1

    # print(sorted(nums, key=cmp_to_key(comparator)))
    s = ''.join(sorted(nums, key=cmp_to_key(comparator)))
    return '0' if int(s) == 0 else s



def largestNumber2(nums: List[int]) -> str:
    lst = list(itertools.permutations(nums, len(nums)))
    print(lst)
    max = 0
    for i in lst:
        j = int(''.join(map(str,i)))
        if max < j:
            max = j

    return str(max)


def largestNumber3(nums: List[int]) -> str:
    def compare(a, b):
        if (a + b) < (b + a):
            return True
        else:
            return False

    for i in range(len(nums) - 1):
        for j in range(0, len(nums) - 1 - i):
            if compare(str(nums[j]), str(nums[j + 1])):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    s = ''.join(str(i) for i in nums)
    return '0' if 0 == int(s) else s



print(largestNumber3([3,30,34,5,9]))

# Input
# [10,2,9,39,17]
# Output
# "93917210"
# Expected
# "93921710"