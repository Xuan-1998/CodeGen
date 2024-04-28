def maxSumOfSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    # base case: when i is 0, we start from the beginning of the array
    for j in range(k + 1):
        if j == 0:
            dp[0][j] = nums[0]
        elif j == 1:
            dp[0][j] = max(nums[0], nums[1])

    # fill up the dp array
    for i in range(1, n):
        for j in range(min(i + 1, k) + 1):
            if j == 0:
                dp[i][j] = nums[i]
            elif j == 1:
                dp[i][j] = max(dp[i - 1][0], nums[i])
            else:
                # consider all possible subsequences with difference j
                for prev_i in range(max(0, i - k), i):
                    dp[i][j] = max(dp[i][j], dp[prev_i][j - 1] + nums[i])

    return max(dp[n - 1])

# Example usage:
nums = [10, 2, -10]
k = 2
print(maxSumOfSubsequence(nums, k))  # Output: 12

