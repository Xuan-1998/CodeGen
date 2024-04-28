def longestSubarray(nums):
    n = len(nums)
    res = 0
    for i in range(n):
        count_ones = 0
        for j in range(i, n):
            if nums[j] == 1:
                count_ones += 1
            else:
                res = max(res, count_ones)
                count_ones = 0
        res = max(res, count_ones)
    return res
