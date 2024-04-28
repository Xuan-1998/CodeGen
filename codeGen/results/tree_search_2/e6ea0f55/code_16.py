def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    # Base case: when k = 0, we consider subsequences with no gaps
    for i in range(n):
        dp[i][0] = max(dp[i-1][0], nums[i]) if i > 0 else nums[0]

    # Fill up the dp table using a bottom-up approach
    for i in range(1, n):
        for j in range(min(i, k) + 1):
            # For each subsequence ending at index i with difference at most j
            dp[i][j] = max(dp[i-1][j], nums[i] + dp[i-j-1][j-1]) if j > 0 else nums[i]

    return max(dp[-1])

# Example usage:
nums = list(map(int, input().split()))
k = int(input())
print(maxSumSubsequence(nums, k))
