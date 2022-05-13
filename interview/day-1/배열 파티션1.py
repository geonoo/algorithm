from typing import List


def arrayPairSum(nums: List[int]) -> int:
    list = sorted(nums)
    print(list)
    return list[0] + list[-2]

def array_pair_sum(nums: List[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        # 짝수 번째 값의 계산
        if i % 2 == 0:
            sum += n
    return sum


print(array_pair_sum([6,2,6,5,1,2]))