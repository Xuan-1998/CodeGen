def maximum_ones(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    max_len = 0
    left = 0

    for i in range(n):
        if nums[i] == 1:
            dp[i + 1] = max(dp[i], dp[left] + 1) if left <= i else 1
            if dp[i + 1] > max_len:
                max_len = dp[i + 1]
            if left <= i and nums[i] != nums[left]:
                left = i
        else:
            dp[i + 1] = 0
            left = i

    return max_len - 1
