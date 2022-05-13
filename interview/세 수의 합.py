import itertools
from typing import List


def threeSum(nums: List[int]):
    list = []
    for a in itertools.combinations(sorted(nums), 3):
        if sum(a) == 0:
            list.append(a)
    print(set(list))


print(threeSum([-1,0,1,2,-1,4]))