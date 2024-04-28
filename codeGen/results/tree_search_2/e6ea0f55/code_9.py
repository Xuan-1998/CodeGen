def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    # Base case: k = 0, no gaps allowed
    max_sum = nums[0]
    for i in range(1, n):
        if nums[i] > max_sum:
            max_sum = nums[i]
        dp[i][0] = max_sum

    for diff in range(1, k + 1):
        for i in range(diff, n):
            for j in range(i - diff, i):
                dp[i][diff] = max(dp[i][diff], dp[j][diff - 1] + nums[i])
                if i == diff:
                    break

    return max(dp[-1])

# Example usage
nums = [10, 12, 5, 3, 20, 15]
k = 2
print(maxSumSubsequence(nums, k))  # Output: 35
