import itertools
from typing import List


def threeSum2(nums: List[int]):
    lists = []
    for a in itertools.combinations(sorted(nums), 3):
        if sum(a) == 0:
            lists.append([*a])

    rtn = []
    for l in lists:
        if l not in rtn:
            rtn.append(l)
    return rtn


# print(threeSum([-1,0,1,2,-1,4]))



def threeSum(nums: list) -> list:
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 간격을 좁혀가며 합 sum 계산
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # sum = 0인 경우이므로 정답 및 스킵 처리
                results.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return results

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))  # [[-1, -1, 2], [-1, 0, 1]]

