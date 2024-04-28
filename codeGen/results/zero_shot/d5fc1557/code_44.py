def longestSubarray(nums):
    n = len(nums)
    res = 0
    count = 0
    max_count = 0
    for i in range(n):
        if nums[i] == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count
