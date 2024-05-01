def distinct_sum_sums(nums):
    n = len(nums)
    dp = [0] * (sum(nums) + 1)
    for num in nums:
        for i in range(sum(nums), num - 1, -1):
            dp[i] += dp[i - num]
    return list(set([i for i in range(1, sum(nums) + 1) if dp[i]]))
