def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if i == 1:
                dp[i][j] = nums[0]
            elif j >= 1 and abs(nums[i - 1] - nums[i - 2]) <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 2][j - 1] + nums[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    return max(dp[n])

# Example usage
nums = list(map(int, input().split()))
k = int(input())
print(maxSumSubsequence(nums, k))
