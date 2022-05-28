def binary_search_builtin(nums, target):
    from bisect import bisect
    idx = bisect.bisect_left(nums, target)

    if idx < len(nums) and nums[idx] == target:
        return idx
    else:
        return -1