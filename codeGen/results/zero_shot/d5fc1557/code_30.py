def longest_subarray(nums):
    n = len(nums)
    res = 0
    count = 0
    for i in range(n):
        if nums[i] == 1:
            count += 1
            res = max(res, count)
        else:
            count = 0
    return res
