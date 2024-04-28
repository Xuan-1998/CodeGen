def longestSubarray(nums):
    n = len(nums)
    res, cnt = 0, 0
    for i in range(n):
        if nums[i] == '1':
            cnt += 1
        else:
            res = max(res, cnt)
            cnt = 0
    return max(res, cnt)
