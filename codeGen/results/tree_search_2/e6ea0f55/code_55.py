def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if j == 0:
                dp[i][j] = nums[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], nums[i - 1] + dp[i - j - 1][j - 1])

    return max(max(row) for row in dp)

# Example usage
nums = list(map(int, input().split()))
k = int(input())
print(maxSumSubsequence(nums, k))
