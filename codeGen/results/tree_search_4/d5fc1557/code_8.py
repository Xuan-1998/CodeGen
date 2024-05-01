def longest_subarray(nums):
    n = len(nums)
    dp = [0] * n
    memo = {}

    def helper(i):
        if i in memo:
            return memo[i]
        if nums[i] == 1:
            dp[i] = max(dp[i-1], dp[i-1] + 1) if i > 0 else 1
        else:
            dp[i] = max(dp[i-1], 0)
        memo[i] = dp[i]
        return dp[i]

    result = 0
    for i in range(1, n):
        result = max(result, helper(i))
    return result if nums[0] == 1 else 0
