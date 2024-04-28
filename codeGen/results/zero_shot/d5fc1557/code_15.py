def longestSubarray(nums):
    n = len(nums)
    ans = 0
    i, j = 0, 0
    while j < n:
        if nums[j] == '1':
            j += 1
        else:
            if j - i > ans:
                ans = j - i
            i = j + 1
    return max(ans, j - i)
