def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    # Initialize the base case: maximum sum of an empty subsequence is 0
    dp[0][0] = 0

    for i in range(1, n):
        for j in range(min(i, k), -1, -1):
            # Transition relationship: max(dp[i-1][k] + nums[i], k in range(0, min(i, j+1)))
            dp[i][j] = max(dp[i-1][min(j, k)] + nums[i], sum(nums[:i+1]))

    return max(max(row) for row in dp)

