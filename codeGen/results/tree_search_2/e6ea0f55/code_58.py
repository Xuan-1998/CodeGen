def max_sum_subsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    # Base case: single-element subsequences
    dp[0][0] = nums[0]

    for i in range(1, n):
        for j in range(min(i+1, k)+1):
            if j == 0:
                dp[i][j] = nums[i]
            else:
                dp[i][j] = max(dp[i-1][j-1] + nums[i], dp[i-k][j-1] + sum(nums[i-k:i+1]))

    return max(dp[n-1])
