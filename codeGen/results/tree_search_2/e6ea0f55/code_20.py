def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    # Base case: when the subsequence starts at index 0 or ends at index n-1
    for i in range(k+1):
        dp[0][i] = nums[0]
        if i > 0:
            dp[n-1][i] = max(dp[n-2][i-1] + nums[n-1], dp[n-1][i-1])

    # Fill up the dynamic programming table
    for i in range(1, n):
        for j in range(min(i, k)+1):
            if j == 0:
                dp[i][j] = max(dp[i-1][j], nums[i])
            else:
                dp[i][j] = max(dp[i-1][j-1] + nums[i], dp[i-1][j])

    # Find the maximum sum
    max_sum = 0
    for i in range(n):
        for j in range(k+1):
            if dp[i][j] > max_sum:
                max_sum = dp[i][j]

    return max_sum


# Test your function
nums = list(map(int, input().split()))
k = int(input())
print(maxSumSubsequence(nums, k))
