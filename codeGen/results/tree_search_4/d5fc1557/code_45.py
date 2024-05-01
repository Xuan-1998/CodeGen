def maximum_ones(nums):
    dp = [(i, i) for i in range(len(nums)) if nums[i] == 1]
    for i, (start, end) in enumerate(dp):
        while start > 0 and nums[start - 1] == 1:
            start -= 1
        while end < len(nums) - 1 and nums[end + 1] == 1:
            end += 1
        dp[i] = (start, end)
    max_len = 0
    for start, end in dp:
        max_len = max(max_len, end - start + 1)
    return max_len
