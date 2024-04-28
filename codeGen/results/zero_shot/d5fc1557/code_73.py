def longestSubarray(nums):
    n = len(nums)
    res = 0
    ones = 0
    start = 0
    for end in range(n):
        if nums[end] == 1:
            ones += 1
        while ones > 1:
            if nums[start] == 1:
                ones -= 1
            start += 1
        res = max(res, end - start + 1)
    return res
